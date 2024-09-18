from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'image', 'long_description', 'bid_end_time']





class ReviewForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'profile_image']  # Adjust fields based on your model
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Review',
                'rows': 5,
                'required': True
            }),
            'profile_image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'required': True
            }),
        }
    def save(self, commit=True):
        # Get the instance of the review, but don't save it yet
        review = super().save(commit=False)
        # Automatically set the category to 'client-review'
        review.category = 'client-review'
        if commit:
            review.save()
        return review
        
