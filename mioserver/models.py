from os import path
from django.db import models
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


class ProductType(models.Model):
    name = models.CharField(max_length=80)
    static_dir = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def get_upload_to(instance, filename):
    return path.join(instance.image_product_type.static_dir.__str__(), filename)


class Image(models.Model):
    author = models.CharField(max_length=100)
    image_product_type = models.ForeignKey(
        ProductType, on_delete=models.DO_NOTHING)
    image_file = models.ImageField(
        upload_to=get_upload_to, null=True, storage=OverwriteStorage())
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
