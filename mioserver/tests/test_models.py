from django.test import TestCase
from mioserver.models import Image


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
