from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'products']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)

    class Meta:
        model = Product
        fields = [
            'uuid',
            'name',
            'brand',
            'description',
            'slug',
            'img',
            'quantity',
            'price',
            'discount',
            'on_warehouse',
            'category',
        ]
