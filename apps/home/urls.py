from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from apps.home.views import HomeView

app_name = "admin"

urlpatterns = [
    path("", lambda request: redirect('admin:home')),

    path(
        "home/",
        login_required(HomeView.as_view(template_name="admin_home.html")),
        name="home",
    ),
]