# Renderizacion Template
from web_project import TemplateLayout
from django.views.generic import TemplateView
from web_project.template_helpers.theme import TemplateHelper

from auth.views import AuthView

# Authenticacion
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect

# Modelos
from django.contrib.auth.models import User

class LoginView(AuthView):
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")

        return super().get(request)
    
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get("email-username")
            password = request.POST.get("password")

            print(username)
            print(password)

            if not (username and password):
                messages.error(request, "Please enter your username and password.")
                return redirect("login")

            if "@" in username:
                user_email = User.objects.filter(email=username).first()
                if user_email is None:
                    messages.error(request, "Please enter a valid email.")
                    return redirect("login")
                username = user_email.username

            user_email = User.objects.filter(username=username).first()
            if user_email is None:
                messages.error(request, "Please enter a valid username.")
                return redirect("login")

            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                # Login the user if authentication is successful
                login(request, authenticated_user)

                # Redirect to the page the user was trying to access before logging in
                if "next" in request.POST:
                    return redirect(request.POST["next"])
                else: 
                    return redirect("admin-home")
            else:
                messages.error(request, "Please enter a valid username.")
                return redirect("login")
