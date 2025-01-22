from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser
from django.contrib import messages


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
                return redirect('viewall')
                # return redirect('superuser_dashboard')
               

            
            elif user.is_staff_user:
                # print("hiii")
                return redirect('viewallstaff')
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
   if request.user.is_authenticated:
        logout(request)  # Logs out the authenticated user
        messages.success(request, "You have successfully logged out.")
   return redirect('login')  # Redirect to the login page (or any other page)


def gotohome(request):
    return render(request, 'index.html')




