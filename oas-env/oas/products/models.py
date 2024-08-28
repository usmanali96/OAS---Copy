from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):  # Rename from Products to Product
    title = models.CharField(max_length=60)
    description = models.TextField()
    category = models.CharField(max_length=60)
    image = models.FileField(max_length=60, upload_to="products/", null=True)

    def __str__(self):
        return self.title




class Cart(models.Model):  # Ensure this model is defined
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

class CartItem(models.Model):  # Ensure this model is defined
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"