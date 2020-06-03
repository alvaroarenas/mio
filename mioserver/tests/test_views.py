from rest_framework.test import APIRequestFactory
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from mioserver.views import ProductListCreate


class ViewTest(TestCase):
    def test_product(self):
        requestFactory = APIRequestFactory()
        request = requestFactory.get('/api/product/')
        response = ProductListCreate.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
