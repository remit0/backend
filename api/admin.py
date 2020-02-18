from django.contrib import admin

from .models import Product, Rating, Image


admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Image)
