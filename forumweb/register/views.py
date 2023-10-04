from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from register.forms import UpdateForm
from django.contrib.auth import logout as lt
from main.models import Author,Post
from django.contrib.auth.models import User
from register.checkprofile import profile_completion_required


def signup(request):
    context = {}
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        author_form = UpdateForm(request.POST, request.FILES)

        if user_form.is_valid() and author_form.is_valid():
            user = user_form.save()
            author = author_form.save(commit=False)
            author.user = user
            author.save()

            login(request, user)
            return redirect("home")

    else:
        user_form = UserCreationForm()
        author_form = UpdateForm()

    context.update({
        "user_form": user_form,
        "author_form": author_form,
        "title": "Signup",
    })
    return render(request, "register/signup.html", context)

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    context.update({
        "form": form,
        "title": "Signin",
    })
    return render(request, "register/signin.html", context)

@login_required
def update_profile(request):
    context = {}
    user = request.user
    form = UpdateForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect("home")
        
    context.update({
        "form": form,
        "title": "Update Profile",
    })
    return render(request, "register/update.html", context)

@profile_completion_required
@login_required
def view_profile(request):
    user = request.user
    author = Author.objects.get(user=user)
    user_posts = Post.objects.filter(user=author)
    context = {
        "author" : author,
        "user_posts": user_posts,
    }
    return render(request, "register/viewprofile.html", context)

def other_profile(request, slug):
    author = Author.objects.get(slug=slug)
    user_posts = Post.objects.filter(user=author)
    return render(request, "register/otherprofile.html", {'author': author,"user_posts": user_posts})

@login_required
def logout(request):
    lt(request)
    return redirect("home")

@profile_completion_required
@login_required
def edit_profile(request):
    author = get_object_or_404(Author, user=request.user)

    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UpdateForm(instance=author)

    context = {
        'form': form
    }

    return render(request, 'register/editprofile.html', context)
