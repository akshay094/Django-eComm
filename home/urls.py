from django.urls import path
from . import views
from .models import Products

urlpatterns = [
    path('', views.homepage , name = 'hompage'),
    path("login", views.login , name="login"),
    path("signup", views.signup , name="signup"),
    path("cartpage", views.cartpage, name="cartpage")
]