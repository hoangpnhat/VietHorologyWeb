from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import BlogModel
# Create your views here.
def home(request):
    return render(request,'home.html')
def lastest(request):
    return render(request,'latest.html')
def login(request):
    return render(request,'login.html')
    
