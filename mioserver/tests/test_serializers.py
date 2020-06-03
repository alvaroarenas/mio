from django.test import TestCase
from mioserver.models import Image, ProductType, Product
from mioserver.serializers import ProductSerializer, ImageSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from rest_framework.test import APIRequestFactory


class SerializerTest(TestCase):
    def setUp(self):
        self.product_result = {
            'id': 1,
            'name': 'Claudia the top model',
            'description': 'A german top model who conquered the world',
            'image_url': 'http://testserver/media/model/claudiaSchieffer.jpg'
        }

        self.product_type = ProductType.objects.create(
            name='TopModel', static_dir='model')
        im_io = BytesIO()
        im_file = InMemoryUploadedFile(
            im_io, None, 'claudiaSchieffer.jpg', 'image/jpeg', len(im_io.getvalue()), None)

        self.image = Image.objects.create(
            author='Alex Webb',
            original_url='https://example.com/awesome.jpg',
            image_file=im_file,
            image_product_type=self.product_type)

        self.product = Product.objects.create(
            name=self.product_result['name'],
            description=self.product_result['description'],
            image=self.image,
            product_type=self.product_type
        )

        reqFactory = APIRequestFactory()
        req = reqFactory.get('/api/product/')
        self.serializedProduct = ProductSerializer(
            instance=self.product, context={'request': req})

        self.serializedImage = ImageSerializer(instance=self.image)

    def test_fields_product(self):
        self.assertEqual(
            set(self.serializedProduct.data),
            set(['id', 'name', 'description', 'image']))

    def test_imagePath_content(self):
        print(self.serializedProduct.data)
        self.assertEqual(
            self.serializedProduct.data['image'],
            self.product_result['image_url'])

    def test_imageSerializer_imageUrl(self):
        self.assertEqual(
            self.serializedImage.data['image_file'],
            '/media/model/claudiaSchieffer.jpg'
        )
