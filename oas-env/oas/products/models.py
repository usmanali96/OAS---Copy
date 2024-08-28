from django.db import models

class Product(models.Model):  
    title = models.CharField(max_length=60)
    description = models.TextField()
    category = models.CharField(max_length=60)
    image = models.FileField(upload_to="products/", null=True)

    def __str__(self):
        return self.title