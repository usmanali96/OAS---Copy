from django import forms
from .models import Product







class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'image', 'long_description', 'bid_end_time']





class ReviewForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image']
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
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'required': True
            }),
        }

    def save(self, commit=True):
        review = super().save(commit=False)
        review.category = 'client-review'  # Set category to 'client-review'
        if commit:
            review.save()
        return review