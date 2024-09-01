from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'image', 'bid_end_time','price','long_description','display_bids']

    def display_bids(self, obj):
        return "\n".join([f"{bid['name']} (${bid['price']})" for bid in obj.bids])

    display_bids.short_description = 'Bids'

    
    
admin.site.register(Product, ProductAdmin) 


# Register your models here.
