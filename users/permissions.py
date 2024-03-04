from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission class to check if the user is the owner of a profile.

    Attributes:
        message (str): The error message to be displayed if the user is not the owner.
    """
    message = 'You are not the owner of this profile!'

    def has_object_permission(self, request, view, obj):
        """
        Method to check if the user is the owner of the profile object.

        Args:
            request: The request object.
            view: The view object.
            obj: The profile object.

        Returns:
            bool: True if the user is the owner, False otherwise.
        """
        if request.user == obj:
            return True
        return False
