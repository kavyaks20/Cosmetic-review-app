from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rimage', 'rating']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            }  # to make the text area bigger
        