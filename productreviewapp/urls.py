from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home/',views.home ,name='home'),
    path('about/',views.about ,name='about'),
    path('suproducts/',views.addproduct ,name='products'),
    path('collections/',views.collections ,name='collections'),
    path('blog/',views.blog ,name='blog'),
    path('contact/',views.contactus ,name='contact'),
    path('staff_review/<int:pk>',views.addreview ,name='staff_review'),
    path('product_detail/<int:pk>',views.product_detail ,name='staff_pro_detail'),
    path('viewall/',views.view_allsuperproduct,name='viewall'),
    path('viewallstaff/',views.viewallstaffproduct,name='viewallstaff'),
    path('viewallend/',views.enduser_dashboard,name='viewallend'),

    

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)