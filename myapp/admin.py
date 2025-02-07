from django.contrib import admin
from .models import Item, ContactMessage, Order

admin.site.register(Item)
admin.site.register(ContactMessage)
admin.site.register(Order)