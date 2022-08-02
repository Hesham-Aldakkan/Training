from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from quest import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from backend.models import User, UserManager
from django.contrib.auth.forms import UserCreationForm
from .models import User
#from .models import User
# Create your views here.



def home(request):
    return render(request, "webapp/index.html")

def signup(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        
        myuser = User.objects.create_user(username, email, phone, password)

        myuser.save()

        messages.success(request, "Account has created successfully")

        return redirect('signin')

    return render(request, "webapp/signup.html")

def signin(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username = username1, password = pass1)
        if user is not None:
            return redirect('userPage')
        else:
            messages.error(request, "Not found")
            return redirect('signin')

    return render(request, "webapp/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "signed out")
    return redirect('home')


def userPage(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "logged out successfully")

    return render(request, "webapp/userPage.html")