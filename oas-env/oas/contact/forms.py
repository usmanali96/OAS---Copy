
from django import forms
from contact.models import Contact


class contactForm(forms.Form):
    name = forms.CharField(max_length=30, label='Name')
    email = forms.CharField(max_length=100, label='Email')
    phone = forms.CharField(max_length=13, label='Phone')
    content = forms.CharField(widget=forms.Textarea, label='Message')

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'content']
