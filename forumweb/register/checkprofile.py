from django.contrib.auth.decorators import user_passes_test
from main.models import Author
from django.shortcuts import redirect

def check_profile_completion(user):
    if not user.is_authenticated:
        return True

    try:
        author = Author.objects.get(user=user)
        return author.fullname and author.bio
    except Author.DoesNotExist:
        return False

def profile_completion_required(view_func):
    def check_profile_completion(user):
        if not user.is_authenticated:
            return True

        try:
            author = Author.objects.get(user=user)
            return author.fullname and author.bio
        except Author.DoesNotExist:
            return False

    def decorated_view_func(request, *args, **kwargs):
        if not check_profile_completion(request.user):
            return redirect('update_profile')
        return view_func(request, *args, **kwargs)

    return decorated_view_func
    