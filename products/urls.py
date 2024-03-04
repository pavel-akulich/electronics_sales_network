from django.urls import path

from products.api_views.product import ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('product/detail/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product-delete'),
]
