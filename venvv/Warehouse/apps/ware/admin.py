from django.contrib import admin
from .models import Order, Profile, Product

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Profile)