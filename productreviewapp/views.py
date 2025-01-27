from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from django.db.models import Avg


# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')
def collections(request):
    product = Product.objects.all()
    reviews=Review.objects.all()
    return render(request, 'collections.html', {'product': product, 'reviews': reviews})

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

def editproduct(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect ('viewall')
    else:
        form= ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form':form,'product':product})


def deleteproduct(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('viewall')
    return render(request, 'delete_product.html', {'product': product})
# end superuser----->



#staff user---->
@login_required   #decorator for checking the authorized users
def addreview(request,pk):
    product = get_object_or_404(Product, pk=pk)  # Fetch the product by primary key

    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES) 
        if form.is_valid():
            # form.save()
            review = form.save(commit=False)
            review.product = product 
            review.reviewer = request.user
            review.save()
            return redirect('staff_pro_detail',pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)  # Fetch the specific product by its primary key
    reviews = Review.objects.filter(product=product)
    avg_rating= reviews.aggregate(Avg('rating'))['rating__avg']
    
    # print("hiiiiii",product,reviews)
    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating
    })
    

def viewallstaffproduct(request):
   
    product = Product.objects.all()
    reviews=Review.objects.all()
    return render(request, 'staff_dashboard.html', {'product': product,'reviews':reviews})



# End user section ------>
def enduser_dashboard(request):
    product = Product.objects.all()
    reviews=Review.objects.all()
    return render(request,'enduser_dashboard.html',{'product':product,'reviews':reviews})
    # reviews= Review.objects.all()

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact.html',{'form':form})
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})



    

