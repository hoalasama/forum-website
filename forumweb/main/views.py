from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Comment, Post, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse

def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    last_post = Post.objects.latest("date")

    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "title": "Home Page"
    }
    return render(request, "forums.html", context)

def detail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    author = None
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)
    if request.method == "POST":
        if "comment-form" in request.POST:
            comment = request.POST.get("comment")
            new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
            post.comments.add(new_comment.id)

        if "reply-form" in request.POST:
            reply = request.POST.get("reply")
            comment_id = request.POST.get("comment-id")
            comment_obj = Comment.objects.get(id=comment_id)
            new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
            comment_obj.replies.add(new_reply.id)

    context = {
        "post":post,
        "title": post.title
    }
    update_views(request, post)

    return render(request, "detail.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts":posts,
        "forum": category,
        "title": "Posts"
    }

    return render(request, "posts.html", context)

@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "title": "Create New Post"
    })
    return render(request, "create_post.html", context)
@login_required
def delete_post(request, post_id=None):
    post_to_delete = get_object_or_404(Post, id=post_id)
    
    if post_to_delete.user.user != request.user:
        return redirect('home')
    elif request.method == 'POST':
        post_to_delete.delete()
        return redirect('home')

    context = {
        'post_id': post_id,
        'user' : request.user,
    }
    return render(request, 'delete_post.html', context)
    #url = reverse('delete_post', args=[post_id])
def my_view(request, post_id):
    post_id = Post.objects.get(id=post_id)
    url = reverse('delete_post', args=[post_id])

def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "Latest 10 posts"
    }

    return render(request, "latest-posts.html", context)

def search_result(request):
    query = request.GET.get('query', '')
    results = Post.objects.filter(title__icontains=query)

    context = {
        'query': query,
        'objects': results
    }

    return render(request, 'search.html', context)

def edit_comment(request, comment_id, post_slug):
    comment = get_object_or_404(Comment, id=comment_id)
    slug = post_slug
    if request.method == 'POST':
        new_content = request.POST.get('new_content')
        comment.content = new_content
        comment.save()
        return redirect('detail', slug)

    return render(request, 'register/editcomment.html', {'comment': comment})

def edit_reply(request, reply_id, post_slug):
    comment = get_object_or_404(Reply, id=reply_id)
    slug = post_slug
    if request.method == 'POST':
        new_content = request.POST.get('new_content')
        comment.content = new_content
        comment.save()
        return redirect('detail', slug)

    return render(request, 'register/editreply.html', {'reply': comment})


def tagged_posts(request, tag_slug):
    tag = tag_slug.split('/')[-1]
    posts = Post.objects.filter(tags__slug=tag_slug)
    return render(request, 'tagged_posts.html', {'tag': tag,'posts': posts})