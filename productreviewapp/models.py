from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from usersapp.models import CustomUser

# Create your models here.

# categories are makeup,skincare,hair and nail
class Category(models.Model):
    cname = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.cname
    
# subcateories all products
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    # review = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='images')
    slug= models.SlugField(null=True,blank=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True,related_name='products')
    def __str__(self):
        return self.name
 
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews',null=True,blank=True)
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.TextField(null=True,blank=True,)
    rimage = models.ImageField(upload_to='review_images/', null=True, blank=True)
    rating = models.PositiveIntegerField(default=1,null=True,blank=True)  # Rating out of 5NULL
    def __str__(self):
        return self.product.name
class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name