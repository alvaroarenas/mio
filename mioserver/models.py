from os import path
from django.db import models
from django.core.files.storage import FileSystemStorage


class ProductType(models.Model):
    name = models.CharField(max_length=80)
    static_dir = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    author = models.CharField(max_length=100)
    image_product_type = models.ForeignKey(
        ProductType, on_delete=models.DO_NOTHING)
    image_file = models.ImageField()
    original_url = models.URLField()
    nickname = models.CharField(max_length=60, null=True)

    @property
    def filename(self):
        return path.basename(self.image_file.name)

    def __str__(self):
        return self.filename


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

    def __str__(self):
        return self.name
