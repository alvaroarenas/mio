from os import path
from django.db import models


class Image(models.Model):
    author = models.CharField(max_length=100)
    filename = models.URLField()
    original_url = models.URLField()

    def __str__(self):
        return self.filename


class ProductType(models.Model):
    name = models.CharField(max_length=80)
    static_dir = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ForeignKey(Image, null=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(
        ProductType, null=True, on_delete=models.CASCADE)

    @property
    def imagePath(self):
        if(self.image):
            return self.image.filename

        return ''
