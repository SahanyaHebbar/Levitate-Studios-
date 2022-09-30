from django.shortcuts import render,HttpResponse
import django.contrib.staticfiles
# Create your views here.
def home(request):
    return render(request, 'home.html')

def book(request):
    return render(request, 'book.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

