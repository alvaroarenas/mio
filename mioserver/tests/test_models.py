from django.test import TestCase
from mioserver.models import Image, Product, ProductType
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from unittest.mock import patch

# import pytest
# from mixer.backend.django import mixer
# pytestmark = pytest.mark.django_db


# @patch('storages.backends.s3boto3.S3Boto3Storage')
class ImageTest(TestCase):
    def setUp(self):
        im_io = BytesIO()
        top_model_type = ProductType.objects.create(
            name='TopModel', static_dir='model')
        Image.objects.create(
            author='Claudia Schieffer',

            image_file=InMemoryUploadedFile(
                im_io, None, 'claudiaSchieffer.jpg', 'image/jpeg', len(im_io.getvalue()), None),

            image_product_type=top_model_type,
            nickname='hun7er',
            original_url='https://example.com/claudia.jpg')

    def test_it_has_model_fields(self):
        image = Image.objects.get(author='Claudia Schieffer')
        self.assertEqual(image.author, 'Claudia Schieffer')
        self.assertIn('claudiaSchieffer', image.filename)
        self.assertEqual(image.original_url, 'https://example.com/claudia.jpg')
        self.assertEqual(image.nickname, 'hun7er')

    def test_str_prints_the_filename(self):
        image = Image.objects.get(author='Claudia Schieffer')
        self.assertIn('claudiaSchieffer', image.__str__())


class ProductTest(TestCase):
    def setUp(self):
        im_io = BytesIO()
        top_model_type = ProductType.objects.create(
            name='TopModel', static_dir='model')
        image = Image.objects.create(
            author='Claudia Schieffer',
            image_file=InMemoryUploadedFile(
                im_io, None, 'claudiaSchieffer.jpg', 'image/jpeg', len(im_io.getvalue()), None),
            image_product_type=top_model_type,
            original_url='https://example.com/claudia.jpg')

        carType = ProductType.objects.create(name='Car', static_dir='car')

        Product.objects.create(
            name='Awesome car',
            description="This is an awesome car",
            image=image,
            product_type=carType
        )

    def test_it_has_all_fields(self):
        product = Product.objects.get(name='Awesome car')
        self.assertEqual('Awesome car', product.name)
        self.assertEqual(product.description, 'This is an awesome car')
        self.assertIn('claudiaSchieffer', product.imagePath)

    def test_it_has_imagePath_empty_when_null_image(self):
        product = Product.objects.get(name='Awesome car')
        product.image = None
        self.assertEqual(product.imagePath, '')

    def test_product_lists_name(self):
        product = Product.objects.get(name='Awesome car')
        self.assertEqual(product.__str__(), 'Awesome car')


class ProductTypeTest(TestCase):
    def test_it_has_all_fields(self):
        carType = ProductType.objects.create(name='Car', static_dir='car')
        self.assertEqual(carType.name, 'Car')
        self.assertEqual(carType.static_dir, 'car')

    def test_str_prints_the_filename(self):
        carType = ProductType.objects.create(name='Car', static_dir='car')
        self.assertEqual(carType.__str__(), 'Car')
