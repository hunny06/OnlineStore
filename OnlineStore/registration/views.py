from django.shortcuts import render
from .forms import SignUpForm, LogInForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        # form = SignUpForm()
    else:
        form = SignUpForm()
    context_data = {"form":form}
    return render(request, "registration/signup.html", context_data)

def login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username =username, password=password )
            if user != None:
                login(request,user)
            
    form = LogInForm()
    context_data = {"form":form}
    return render(request, "registration/login.html", context_data)