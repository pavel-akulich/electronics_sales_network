from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from trading_networks.models import Network
from trading_networks.paginators import NetworkPaginator
from trading_networks.permissions import IsActiveEmployee, IsSuperUser
from trading_networks.serializers.network import NetworkSerializer


class NetworkCreateAPIView(generics.CreateAPIView):
    """
    API view for creating a new network.

    Attributes:
        serializer_class (Serializer): The serializer class used for network creation.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and an active employee.
    """
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class NetworkListAPIView(generics.ListAPIView):
    """
    API view for listing all networks.

    Attributes:
        serializer_class (Serializer): The serializer class used for serializing networks.
        queryset (QuerySet): The queryset containing all networks.
        pagination_class (Paginator): The paginator class used for pagination.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and an active employee.
        filter_backends (list): The filter backends used for filtering the queryset.
        filterset_fields (tuple): The fields allowed for filtering.
        ordering_fields (tuple): The fields allowed for ordering.
    """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    pagination_class = NetworkPaginator
    permission_classes = [IsAuthenticated & IsActiveEmployee]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country',)
    ordering_fields = ('network_level',)


class NetworkRetrieveAPIView(generics.RetrieveAPIView):
    """
    API view for retrieving a single network.

    Attributes:
        serializer_class (Serializer): The serializer class used for serializing networks.
        queryset (QuerySet): The queryset containing all networks.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and an active employee.
    """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class NetworkUpdateAPIView(generics.UpdateAPIView):
    """
    API view for updating a network.

    Attributes:
        serializer_class (Serializer): The serializer class used for updating networks.
        queryset (QuerySet): The queryset containing all networks.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and an active employee.
    """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee]

    def update(self, request, *args, **kwargs):
        """
        Custom method to update a network instance.
        This method overrides the default update behavior to disallow updating the 'debt' field.
        """
        if 'debt' in request.data:
            del request.data['debt']
        return super().update(request, *args, **kwargs)


class NetworkDestroyAPIView(generics.DestroyAPIView):
    """
    API view for deleting a network.

    Attributes:
        queryset (QuerySet): The queryset containing all networks.
        permission_classes (list): The permission classes required for accessing this view.
            Requires the user to be authenticated and a superuser.
    """
    queryset = Network.objects.all()
    permission_classes = [IsAuthenticated & IsSuperUser]
