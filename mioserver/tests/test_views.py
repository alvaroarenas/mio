from rest_framework.test import APIRequestFactory
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from mioserver.views import ProductListCreate, ProductListFiltered
from unittest.mock import patch


class ViewTest(TestCase):
    def test_product(self):
        requestFactory = APIRequestFactory()
        request = requestFactory.get('/api/product/')
        response = ProductListCreate.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch("mioserver.models.Product.objects.filter", autospec=True)
    def test_filtered_product(self, mock):
        requestFactory = APIRequestFactory()
        request = requestFactory.get('/api/product/rocket/')
        response = ProductListFiltered.as_view()(request, product_type='car')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock.assert_called_with(product_type__name__iexact='car')
