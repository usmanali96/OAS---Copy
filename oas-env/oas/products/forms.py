from django import forms
from .models import Product







from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)










class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'image', 'long_description', 'bid_end_time']





class ReviewForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image']  # Category is omitted from the form
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
        review.category = 'client-review'  # Set category to 'client-review' only for this form
        if commit:
            review.save()
        return review