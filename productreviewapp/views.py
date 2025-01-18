from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db import models
from django.contrib.auth.models import AbstractUser


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

def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            a= form.save(commit=False)
            a.save()
            return redirect('viewall')
    else:

        form= ProductForm()
        return render(request, 'add_product.html', {'form': form})

def view_allsuperproduct(request):
    product = Product.objects.all()
    return render(request, 'superuser_dashboard.html', {'product': product})
