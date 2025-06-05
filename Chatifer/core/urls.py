from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path('sign_up/', views.login_or_signup, name="sign_up"),
    path('log_in/', views.login_or_signup, name="log_in"),
]   