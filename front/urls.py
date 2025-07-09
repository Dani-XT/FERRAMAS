from django.urls import path, include
from django.shortcuts import redirect

app_name = "front"

urlpatterns = [
    path("home/", include("front.home.urls")),
    # path("home/", include("front.carrito.urls")),
    path("home", include("front.ecommerce.urls")),
    

    path("", lambda request: redirect('front:home')),
]