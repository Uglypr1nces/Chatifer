from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "home.html")


def login_or_signup(request):
    return render(request, "login.html")
