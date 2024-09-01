from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'image', 'bid_end_time','price','long_description']
    
    
admin.site.register(Product, ProductAdmin) 


# Register your models here.
