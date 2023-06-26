from django.urls import path
from .views import home, detail, posts, create_post, latest_posts, delete_post

urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("delete_post/<int:id>", delete_post, name="delete_post"),

]