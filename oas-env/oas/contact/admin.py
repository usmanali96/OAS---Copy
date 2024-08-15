from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'content',]


admin.site.register(Contact, ContactAdmin)
# Register your models here.
