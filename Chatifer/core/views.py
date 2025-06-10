from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from threading import Thread
from .models import User
from .client import ChatClient

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
        server_port = int(request.POST.get("port"))

        print(f"connecting to.. {server_ip}, {server_port}")

        user_client = ChatClient(server_ip,server_port)
        user_client.connect()
        t = Thread(target=user_client.listen) #create thread to server listener so it doesnt disrupt the rest of the code
        t.start()

        user_client.send_message("Hello")

        return HttpResponse("Recieved info")
