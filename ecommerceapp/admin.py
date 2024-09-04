from django.contrib import admin
from .models import storetype,items,itemsdetails, cart
# Register your models here.
admin.site.register(storetype)
admin.site.register(items)
admin.site.register(itemsdetails)

admin.site.register(cart)