from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):  # Rename from Products to Product
    title = models.CharField(max_length=60)
    description = models.TextField()
    category = models.CharField(max_length=60)
    image = models.FileField(max_length=60, upload_to="products/", null=True)
    bid_end_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

