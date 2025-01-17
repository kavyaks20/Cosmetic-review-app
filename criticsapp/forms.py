from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'image', 'rating']