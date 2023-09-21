from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Comment, Post, Reply, Vote
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from register.checkprofile import profile_completion_required
from django.db.models import Q
from .forms import PostEditForm

@profile_completion_required
def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    
    #posts = Post.objects.all()
    
    page = request.GET.get("page")
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = Post.objects.filter(
        Q(categories__title__icontains=q) |
        Q(title__icontains=q) |
        Q(content__icontains=q)
    )

    paginator = Paginator(posts, 10)

    try:
        last_post = Post.objects.latest("date")
    except Post.DoesNotExist:
        last_post = None

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "posts" : posts,
        "q" : q,
        "title": "Home Page",
    }
    return render(request, "forums.html", context)


def detail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    post = Post.objects.get(pk=post.id)

    author = get_object_or_404(Author, user=request.user)
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
        "title": post.title,
        "author": author,
    }
    update_views(request, post)

    return render(request, "detail.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 10)
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

@profile_completion_required
@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None, request.FILES or None)
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

def my_view(request, post_id):
    post_id = get_object_or_404(Post, id=post_id)
    url = reverse('delete_post', args=[post_id])

def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "Latest 10 posts"
    }

    return render(request, "latest-posts.html", context)

@profile_completion_required
def search_result(request):
    query = request.GET.get('query', '')
    #results = Post.objects.filter(title__icontains=query)
    results = Post.objects.filter(
        Q(title__icontains=query) |  
        Q(content__icontains=query) | 
        Q(user__fullname__icontains=query)  
    )

    context = {
        'query': query,
        'objects': results
    }

    return render(request, 'search.html', context)

@login_required
def edit_post(request, post_id, post_slug):
    post = get_object_or_404(Post, pk=post_id)
    slug = post_slug
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', slug)
    else:
        form = PostEditForm(instance=post)
    
    return render(request, 'register/editpost.html', {'form': form, 'post': post})

@login_required
def edit_comment(request, comment_id, post_slug):
    comment = get_object_or_404(Comment, id=comment_id)
    slug = post_slug
    if request.method == 'POST':
        new_content = request.POST.get('new_content')
        comment.content = new_content
        comment.save()
        return redirect('detail', slug)

    return render(request, 'register/editcomment.html', {'comment': comment})

@login_required
def delete_comment(request, comment_id, post_slug):
    comment = get_object_or_404(Comment, id=comment_id)
    slug = post_slug
    if request.method == 'POST':
        comment.replies.all().delete()
        comment.delete()
        return redirect('detail', slug)
    
    return render(request, 'delete_comment.html', {'comment': comment})

@login_required
def edit_reply(request, reply_id, post_slug):
    comment = get_object_or_404(Reply, id=reply_id)
    slug = post_slug
    if request.method == 'POST':
        new_content = request.POST.get('new_content')
        comment.content = new_content
        comment.save()
        return redirect('detail', slug)

    return render(request, 'register/editreply.html', {'reply': comment})

@login_required
def delete_reply(request, reply_id, post_slug):
    comment = get_object_or_404(Reply, id=reply_id)
    slug = post_slug
    if request.method == 'POST':
        comment.delete()
        return redirect('detail', slug)
    
    return render(request, 'delete_reply.html', {'comment': comment})

def tagged_posts(request, tag_slug):
    tag = tag_slug.split('/')[-1]
    posts = Post.objects.filter(tags__slug=tag_slug)
    return render(request, 'tagged_posts.html', {'tag': tag,'posts': posts})

@login_required
def upvote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    author = Author.objects.get(user=user.id)
    vote, created = Vote.objects.get_or_create(user=author, post=post)
    
    if created or vote.activity_type == Vote.DOWN_VOTE[0]:
        vote.activity_type = Vote.UP_VOTE[0]
        vote.save()
    
    vote_count = post.get_vote_count()
    #return redirect(request.META.get('HTTP_REFERER', ''))
    return JsonResponse({'vote_count': vote_count})
    
    
@login_required
def downvote(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    author = Author.objects.get(user=user.id)
    vote, created = Vote.objects.get_or_create(user=author, post=post)
    
    if created or vote.activity_type == Vote.UP_VOTE[0]:
        vote.activity_type = Vote.DOWN_VOTE[0]
        vote.save()
    
    vote_count = post.get_vote_count()
    #return redirect(request.META.get('HTTP_REFERER', ''))
    return JsonResponse({'vote_count': vote_count})

