from django.shortcuts import render,HttpResponse
import django.contrib.staticfiles
# Create your views here.
def home(request):
    return render(request, 'index.html')

