from django.urls import path

from accounts.views import login_view, logout_view, register_view

app_name = "accounts"

urlpatterns = [
    path("register", register_view, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
]
