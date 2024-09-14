from django import forms
from django.shortcuts import render, redirect
from .models import Product


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea)
    profile_pic = forms.ImageField(required=False)
    product_id = forms.IntegerField(widget=forms.HiddenInput)

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            profile_pic = form.cleaned_data.get('profile_pic')
            product_id = form.cleaned_data['product_id']
            
            # Get the product
            product = Product.objects.get(id=product_id)
            
            # Save review in the product's reviews JSON field
            review = {
                'name': name,
                'comment': comment,
                'profile_pic': profile_pic.url if profile_pic else None
            }
            reviews = product.reviews
            reviews.append(review)
            product.reviews = reviews
            product.save()
            
            return redirect('success_url')  # Replace with your success URL or message

    else:
        form = ReviewForm()

    return render(request, 'your_template.html', {'form': form})