from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path('signup/', views.login_or_signup, name="sign_up"),
    path('login/', views.login_or_signup, name="log_in"),
    path('login/sign_up/', views.sign_up, name="sign_up1"),
    path('login/log_in/', views.log_in, name="log_in1"),
    path('signup/sign_up/', views.sign_up, name="sign_up2"),
    path('signup/log_in/', views.log_in, name="log_in2"),

    path('home/', views.home, name="home"),
    path('home/connect/', views.connect_server, name="connect"),

    path('chat/',views.chat, name="chat"),
    path('chat/send_message/', views.send_message, name="send_message"),
    path('chat/sse_messages/', views.sse_messages, name="sse_messages"),
]   