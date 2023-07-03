from django.urls import path
from .views import home, detail, posts, create_post, latest_posts, delete_post, search_result, edit_comment, edit_reply, tagged_posts, edit_post, upvote, downvote
    
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("post/<post_id>/delete/", delete_post, name="delete_post"),
    path("search/", search_result, name="search_result"),
    path("comment/edit/<int:comment_id>/<post_slug>", edit_comment, name="edit_comment"),
    path("reply/edit/<int:reply_id>/<post_slug>", edit_reply, name="edit_reply"),
    path("post/edit/<int:post_id>/<post_slug>", edit_post, name="edit_post"),
    path("tagged/<slug:tag_slug>/", tagged_posts, name="tagged_posts"),
    path("upvote/<int:post_id>/", upvote, name="upvote"),
    path("downvote/<int:post_id>/", downvote, name="downvote"),
]