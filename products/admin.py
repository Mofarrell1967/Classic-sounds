from django.contrib import admin
from .models import Product

""" To allow us to add products through the admin panel """

admin.site.register(Product)
