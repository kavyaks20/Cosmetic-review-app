from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserLoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('superuser_dashboard')
            elif user.is_staff:
                return redirect('staff_dashboard')
            else:
                return redirect('enduser_dashboard')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def superuser_dashboard(request):
    return render(request, 'superuser_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

@login_required
def enduser_dashboard(request):
    return render(request, 'enduser_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')






# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
# from django.contrib import messages


# # Create your views here.

    
# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         password=request.POST['password']
#         confirm_password=request.POST['confirm_password']
#         if password == confirm_password:
#             try:
#                 user = User.objects.create_user(username=username,email=email,password=password)
#                 messages.success(request,"registration successfull!!!  Please login")
#                 return redirect('login')
#             except:
#                 messages.error(request,"Username already exist!")
#         else:
#             messages.error(request,"Invalid username or password")
#         return render(request,'register.html')


            

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user= authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')         
#         else:
#             messages.error(request,"Invalid username or password")
#     return render(request,'login.html')


# def logout(request):
#     return render('login')