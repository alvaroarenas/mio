from rest_framework import serializers
from .models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    image_file = serializers.ImageField(
        max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Image
        fields = ('id', 'author', 'filename', 'original_url', 'image_file')


class ImageUrlField(serializers.RelatedField):
    def to_representation(self, instance):
        url = instance.image_file.url
        request = self.context.get('request', None)
        return request.build_absolute_uri(url)


class ProductTypeField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name


class ProductSerializer(serializers.ModelSerializer):
    image = ImageUrlField(read_only=True)
    product_type = ProductTypeField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'product_type')
