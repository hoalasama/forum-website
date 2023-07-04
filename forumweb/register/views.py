from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from register.forms import UpdateForm
from django.contrib.auth import logout as lt
from main.models import Author
from django.contrib.auth.models import User
from register.checkprofile import profile_completion_required


def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("update_profile")
    context.update({
        "form":form, 
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
    context = {
        "author" : author
    }
    return render(request, "register/viewprofile.html", context)

def other_profile(request, slug):
    author = Author.objects.get(slug=slug)
    return render(request, "register/otherprofile.html", {'author': author})

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
