from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):  # Rename from Products to Product
    title = models.CharField(max_length=60)
    description = models.TextField()
    category = models.CharField(max_length=60)
    image = models.FileField(max_length=60, upload_to="products/", null=True)
    bid_end_time = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title

