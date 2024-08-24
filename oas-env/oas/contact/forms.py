
from django import forms
from contact.models import Contact


class contactForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label='Your Name')
    email = forms.CharField(max_length=100, label='Your Email')
    phone = forms.CharField(max_length=13, label='Your Phone')
    content = forms.CharField(widget=forms.Textarea, label='Your Message')

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'content']
