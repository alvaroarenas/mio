from django.contrib import admin

# Register your models here.
from mioserver.models import Image, Product, ProductType

admin.site.register(Image)
admin.site.register(Product)
admin.site.register(ProductType)
