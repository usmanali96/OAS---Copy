from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=13,  null=True, blank=True)
    content = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name