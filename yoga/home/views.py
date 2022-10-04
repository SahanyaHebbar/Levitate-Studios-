from operator import sub
from django.shortcuts import render,HttpResponse,redirect
import django.contrib.staticfiles
from django.contrib.auth.models import User 
from django.contrib import auth,messages
import sqlite3

# Create your views here.
current_username = 'Login/Signup'
current_pass =  None
def home(request):
    return render(request, 'index.html',{'current_username':current_username})

def book(request):
    return render(request, 'book.html',{'current_username':current_username})

def aboutUs(request):
    return render(request, 'aboutUs.html',{'current_username':current_username})


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
                return redirect('/')
            else:
                current_username='Login/Signup'
                messages.info(request, 'Incorrect username or password!')
                return render(request,"loginSignup.html",{'current_username':current_username})

        elif request.POST['email']!="" and request.POST['password']!="":      #Signup stuff
            EmailID=request.POST['email']
            Password=request.POST['password']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['Username']
            user = User.objects.create_user(username=username, password=Password, email=EmailID,first_name=first_name,last_name=last_name)
            if request.POST['emailUp']:
                subscribe(EmailID)
            return redirect('/')
    elif request.method=='GET':
        return render(request,"loginSignup.html",{'current_username':current_username})

def contactUs(request):
    return render(request, 'contactUs.html',{'current_username':current_username})

def instructor(request):
    return render(request, 'instructor.html',{'current_username':current_username})

def subscribe(EmailId):
    con=sqlite3.connect('db.sqlite3')
    cur=con.cursor()
    cur.execute("INSERT INTO subEmail VALUES (?)",(EmailId,))
    con.commit()
    con.close()
