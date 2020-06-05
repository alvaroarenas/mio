from .models import Product, Image
from .serializers import ProductSerializer, ImageSerializer
from rest_framework import generics


class ProductListCreate(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListFiltered(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_type = self.kwargs['product_type']
        return Product.objects.filter(product_type__name__iexact=product_type)


class ImageListCreate(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
