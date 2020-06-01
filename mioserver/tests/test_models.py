from django.test import TestCase
from mioserver.models import Image, Product


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

        Product.objects.create(
            name='Awesome car',
            description="This is an awesome car",
            image=image
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
