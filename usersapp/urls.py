from django.urls import path
from . import views



urlpatterns = [
    path('', views.gotohome, name='hompage'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('superuser_dashboard/', views.superuser_dashboard, name='superuser_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('enduser_dashboard/', views.enduser_dashboard, name='enduser_dashboard'),
]
