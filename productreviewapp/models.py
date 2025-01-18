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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    review = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    # subcat=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug= models.SlugField(null=True,blank=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)
    rating = models.PositiveIntegerField(default=1)  # Rating out of 5

class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
