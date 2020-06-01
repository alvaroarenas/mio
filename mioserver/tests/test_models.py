from django.test import TestCase
from mioserver.models import Image, Product, ProductType


class ImageTest(TestCase):
    def setUp(self):
        Image.objects.create(
            author='Claudia Schieffer',
            filename='claudiaSchieffer.jpg',
            original_url='https://example.com/claudia.jpg')

    def test_it_has_model_fields(self):
        image = Image.objects.get(author='Claudia Schieffer')
        self.assertEqual(image.author, 'Claudia Schieffer')
        self.assertEqual(image.filename, 'claudiaSchieffer.jpg')
        self.assertEqual(image.original_url, 'https://example.com/claudia.jpg')


class ProductTest(TestCase):
    def setUp(self):
        image = Image.objects.create(
            author='Claudia Schieffer',
            filename='claudiaSchieffer.jpg',
            original_url='https://example.com/claudia.jpg')

        carType = ProductType.objects.create(name='Car', static_dir='car')

        Product.objects.create(
            name='Awesome car',
            description="This is an awesome car",
            image=image,
            type=carType
        )

    def test_it_has_all_fields(self):
        product = Product.objects.get(name='Awesome car')
        self.assertEqual('Awesome car', product.name)
        self.assertEqual(product.description, 'This is an awesome car')
        self.assertEqual(product.imagePath, 'claudiaSchieffer.jpg')

    def test_it_has_imagePath_empty_when_null_image(self):
        product = Product.objects.get(name='Awesome car')
        product.image = None
        self.assertEqual(product.imagePath, '')


class ProductTypeTest(TestCase):
    def test_it_has_all_fields(self):
        carType = ProductType.objects.create(name='Car', static_dir='car')
        self.assertEqual(carType.name, 'Car')
        self.assertEqual(carType.static_dir, 'car')
