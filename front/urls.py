from django.urls import path, include
from django.shortcuts import redirect

app_name = "front"

urlpatterns = [
    path("", include("front.home.urls")),
    # path("home/", include("front.carrito.urls")),
    path("", include("front.ecommerce.urls")),
    

    path("", lambda request: redirect('front:home')),
]