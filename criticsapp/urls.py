from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home ,name='home'),
    path('about/',views.about ,name='about'),
    path('products/',views.products ,name='products'),
    path('trending/',views.trending ,name='trending'),
    path('blog/',views.blog ,name='blog'),
    path('contact/',views.contact ,name='contact'),
    

]