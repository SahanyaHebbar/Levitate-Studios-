from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
        return redirect('/home')
    else: 
        return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)
            return redirect('/home')
    else: 
        return render(request, 'login.html')
    