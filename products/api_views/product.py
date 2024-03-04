from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.paginators import ProductPaginator
from products.serializers.product import ProductSerializer
from trading_networks.permissions import IsActiveEmployee, IsSuperUser


class ProductCreateAPIView(generics.CreateAPIView):
    """
    API view for creating a new product.

    Attributes:
        serializer_class (Serializer): The serializer class used for product creation.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and an active employee.
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class ProductListAPIView(generics.ListAPIView):
    """
    API view for listing all products.

    Attributes:
        serializer_class (Serializer): The serializer class used for serializing products.
        queryset (QuerySet): The queryset containing all products.
        pagination_class (Paginator): The paginator class used for pagination.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and an active employee.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPaginator
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """
    API view for retrieving a single product.

    Attributes:
        serializer_class (Serializer): The serializer class used for serializing products.
        queryset (QuerySet): The queryset containing all products.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and an active employee.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    API view for updating a product.

    Attributes:
        serializer_class (Serializer): The serializer class used for updating products.
        queryset (QuerySet): The queryset containing all products.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and an active employee.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """
    API view for deleting a product.

    Attributes:
        queryset (QuerySet): The queryset containing all products.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and a superuser.
    """
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated & IsSuperUser]
