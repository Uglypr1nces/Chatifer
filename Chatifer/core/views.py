from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from threading import Thread
from .models import User
from .client import user_client
from django.http import StreamingHttpResponse
import time

latest_message = None

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def login_or_signup(request):
    return render(request, "login.html")

def chat(request):
    return render(request, "chat.html")

@csrf_exempt
def sign_up(request):
     if request.method == "POST":
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(
            first_name=first,
            last_name=last,
            email=email,
            password=password  
        )

        print(f"User: {first} signed up!")
        return HttpResponse("Signed up")

@csrf_exempt
def log_in(request):
     if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')


        try:
            user = User.objects.filter(email=email, password=password).first()
            
            if user:
                return HttpResponse(f"{user.first_name}")
            else:
                return HttpResponse("Couldn't find user")

        except:
            return HttpResponse("Couldnt find user")

     return HttpResponse("Tried Log In")

@csrf_exempt
def connect_server(request):
    if request.method == "POST":
        server_ip = request.POST.get("ip")

        user_client.set_server(server_ip)
        user_client.connect()

        return HttpResponse("Connected to server")

def sse_event_stream():
    global latest_message
    previous = ""
    while True:
        if latest_message != previous:
            yield f"data: {latest_message}\n\n"
            previous = latest_message
        time.sleep(1)

@csrf_exempt
def sse_messages(request):
    return StreamingHttpResponse(sse_event_stream(), content_type='text/event-stream')

@csrf_exempt
def send_message(request):
    global latest_message
    if request.method == "POST":
        msg = request.POST.get("user_message")
        user_name = request.POST.get("user_name")
        latest_message = f"{user_name}: {msg}"  # update global message
        user_client.send_message(latest_message)
        return HttpResponse("Sent message")