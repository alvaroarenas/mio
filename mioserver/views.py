from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
