from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home/',views.home ,name='home'),
    path('about/',views.about ,name='about'),
    path('suproducts/',views.addproduct ,name='products'),
    path('trending/',views.trending ,name='trending'),
    path('blog/',views.blog ,name='blog'),
    path('contact/',views.contact ,name='contact'),
    path('viewall/',views.view_allsuperproduct,name='viewall'),
    path('viewallstaff/',views.viewallstaffproduct,name='viewallstaff'),

    

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)