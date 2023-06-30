from django.urls import path
from .views import home, detail, posts, create_post, latest_posts, delete_post, search_result
from . import views
from register.views import other_profile
urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("post/<post_id>/delete/", delete_post, name="delete_post"),
    path("search/", search_result, name="search_result"),
]