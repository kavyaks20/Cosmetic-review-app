
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def products(request):
    return render(request, 'streams.html')
def trending(request):
    return render(request, 'trending.html')
def blog(request):
    return render(request, 'blog.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')


    
