from django.shortcuts import render,HttpResponse,redirect
import django.contrib.staticfiles
from django.contrib.auth.models import User 
from django.contrib import auth
# Create your views here.
current_username = None
current_pass =  None
def home(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'book.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')


def loginSignup(request):
    global current_username
    global current_pass
    render(request,"loginSignup.html")
    if request.method=='POST':
        if "loginUser" in request.POST:            #login stuff
            user=request.POST['loginUser']
            password=request.POST['loginpass']
            current_username=user
            current_pass=password
            user = auth.authenticate(username=current_username, password=current_pass)
            if user:
                auth.login(request, user)
                return redirect('/home')

        elif request.POST['email']!="" and request.POST['password']!="":      #Signup stuff
            EmailID=request.POST['email']
            Password=request.POST['password']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['Username']
            user = User.objects.create_user(username=username, password=Password, email=EmailID,first_name=first_name,last_name=last_name)
            return redirect('/home')
    elif request.method=='GET':
        return render(request,"loginSignup.html")

def contactUs(request):
    return render(request, 'contactUs.html')

def instructor(request):
    return render(request, 'instructor.html')