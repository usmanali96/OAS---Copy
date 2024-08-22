from django.contrib.auth.forms import UserCreationForm
from django import forms
from contact.models import Contact


class contactForm(UserCreationForm):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=13)
    content = forms.CharField()


    class Meta:
        model = Contact
        fields = ['name', 'email,' 'phone', 'content']
