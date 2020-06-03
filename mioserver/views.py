from .models import Product, Image
from .serializers import ProductSerializer, ImageSerializer
from rest_framework import generics


class ProductListCreate(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageListCreate(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
