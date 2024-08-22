from django.contrib.auth.forms import UserCreationForm
from django import forms
from contact.models import Contact
import contact


class contactForm(UserCreationForm):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=13)
    content = forms.TextField()
    timestamp = forms.DateTimeField(auto_now_add=True)


    class Meta:
        model = contact
        fields = ['name', 'email,' 'phone', 'content']
