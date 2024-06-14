from django.contrib import admin
from django.urls import path, include
import users.views as users_view

app_name = "users"

urlpatterns = [
    path("register/", users_view.register_view, name="register"),
    path("signin/", users_view.signin_view, name="signin"),
    path("logout/", users_view.logout_view, name="logout"),
    path("profile/", users_view.profile, name="profile"),
]
