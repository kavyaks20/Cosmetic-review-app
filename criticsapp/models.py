from django.db import models
from django.utils.text import slugify
# Create your models here.

# categories are makeup,skincare,hair and nail
class Category(models.Model):
    cname = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.cname
    
# subcateories all products
class Products(models.Model):
    pname = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    review = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='images/')
    subcat=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug= models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.pname

    
