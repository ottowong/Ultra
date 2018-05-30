from django.contrib import admin

# Register your models here.
from .models import Type, Product, ProductImage, Colour, ProductColour

admin.site.register(Type)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Colour)
admin.site.register(ProductColour)