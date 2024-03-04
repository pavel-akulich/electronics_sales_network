from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
    Custom permission class to check if the user is a superuser.

    Attributes:
        message (str): The error message to be displayed if the user is not a superuser.
    """
    message = 'You are not a superuser!'

    def has_permission(self, request, view):
        """
        Method to check if the user is a superuser.

        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        if request.user.is_superuser:
            return True
        return False


class IsActiveEmployee(BasePermission):
    """
    Custom permission class to check if the user is an active employee.

    Attributes:
        message (str): The error message to be displayed if the user is not an active employee.
    """
    message = 'You are not a active employee!'

    def has_permission(self, request, view):
        """
        Method to check if the user is an active employee.

        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object.

        Returns:
            bool: True if the user is an active employee, False otherwise.
        """
        return request.user.is_active
