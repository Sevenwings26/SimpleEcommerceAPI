from django.urls import path
from .views import CategoryListCreate, ProductListCreate, ProductDetail, OrderListCreate

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
]
