from django import forms
from django.shortcuts import render, redirect
from .models import Product


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea)
    profile_pic = forms.ImageField(required=False)
    product_id = forms.IntegerField()