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
# superuser------>
def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            product = form.save(commit=False)
            product.added_by = request.user
            product.save()
            return redirect('viewall')
    else:

        form= ProductForm()
    return render(request, 'add_product.html', {'form': form})

def view_allsuperproduct(request):
    product = Product.objects.all()
    return render(request, 'superuser_dashboard.html', {'product': product})
# end superuser----->



#staff user---->
def addreview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            review = form.save(commit=False)
            review.added_by = request.user
            review.save()
            return redirect('viewallstaff')
        else:
            rform = ReviewForm()
        return render(request, 'add_review.html', {'rform': rform})
    
def viewallstaffproduct(request):
    # rproduct = Product.objects.filter(added_by=request.user)
    # product = Product.objects.get(id=product_id)
    rproduct = Product.objects.all()
    return render(request, 'staff_dashboard.html', {'rproduct': rproduct})






    

