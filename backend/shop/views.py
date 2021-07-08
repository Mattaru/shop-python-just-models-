from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
