from django import forms



class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Review', 'rows': 4}), label="Your Review")
