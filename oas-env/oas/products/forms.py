from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    comment = forms.CharField(widget=forms.Textarea, label="Your Review")