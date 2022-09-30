from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home),
    path('book',views.book),
    path('aboutUs',views.aboutUs),
    path('loginSignup',views.loginSignup),
    
]
