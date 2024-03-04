from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from trading_networks.permissions import IsSuperUser
from users.models import User
from users.permissions import IsOwner
from users.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet class for managing User instances.

    Attributes:
        serializer_class (class): The serializer class for serializing User instances.
        queryset (QuerySet): The queryset containing User instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """
        Method to return the permissions required for each action.

        Returns:
            list: List of permission classes.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated & IsSuperUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated & IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated & IsSuperUser | IsOwner]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated & IsOwner | IsSuperUser]
        else:
            permission_classes = [IsAuthenticated & IsSuperUser]
        return [permission() for permission in permission_classes]
