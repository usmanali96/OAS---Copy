from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    category = models.CharField(max_length=60)
    image = models.FileField(max_length=60, upload_to="products/", null=True)

    

# Create your models here.
