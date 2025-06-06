from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path('signup/', views.login_or_signup, name="sign_up"),
    path('login/', views.login_or_signup, name="log_in"),
    path('login/sign_up/', views.sign_up, name="sign_up"),
    path('login/log_in/', views.log_in, name="log_in"),
    path('signup/sign_up/', views.sign_up, name="sign_up"),
    path('signup/log_in/', views.log_in, name="log_in"),
]   