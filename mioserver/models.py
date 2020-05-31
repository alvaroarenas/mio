from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    imagePath = models.CharField(max_length=100)


class Image(models.Model):
    author = models.CharField(max_length=100)
    filename = models.URLField()
    original_url = models.URLField()
