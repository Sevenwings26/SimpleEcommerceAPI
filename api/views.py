from django.shortcuts import render
from rest_framework import generics
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    OrderSerializer
)
from .models import (
    Category, Product, Order
)


# List and Create Categories
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# List and Create Products
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, Update, Delete a Single Product
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# List and Create Orders
class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

