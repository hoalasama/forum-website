from django.urls import path
from .views import signup, signin, update_profile, logout, view_profile, edit_profile, other_profile

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("logout/", logout, name="logout"),
    path("update_profile/", update_profile, name="update_profile"),
    path("view_profile/", view_profile, name="view_profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("other_profile/<slug:slug>/", other_profile, name="other_profile"),
]