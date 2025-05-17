from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

# Views personalizada
from auth.login.views import LoginView


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),

]