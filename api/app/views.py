from django.shortcuts import render
from rest_framework import viewsets
from .models import Products, Categories
from .serialisers import ProductSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer