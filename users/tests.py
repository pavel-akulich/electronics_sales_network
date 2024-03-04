from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):
    """
    Test case class for testing User API endpoints.
    """

    def setUp(self):
        """
        Method to set up the test case.

        Creates a superuser and authenticates the client.
        """
        self.user = User.objects.create(
            email='testmail@gmail.com',
            password='testpassword',
        )

        self.user.is_superuser = True
        self.user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """
        Method to test creating a new user.
        """
        data = {
            "email": "test_user@gmail.com",
            "password": "password123456789"
        }
        response = self.client.post(
            '/users/users/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_user_list(self):
        """
        Method to test listing all users.
        """
        response = self.client.get(
            '/users/users/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    "pk": self.user.pk,
                    "email": self.user.email,
                    "first_name": self.user.first_name,
                    "last_name": self.user.last_name,
                    "phone": None,
                    "country": None,
                    "avatar": None
                }
            ]
        )

    def test_user_update(self):
        """
        Method to test updating user details.
        """
        updated_data = {
            "email": self.user.email,
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "phone": "+123456789",
            "country": "test_country"
        }

        response = self.client.put(
            f'/users/users/{self.user.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_delete(self):
        """
        Method to test deleting a user.
        """
        response = self.client.delete(
            f'/users/users/{self.user.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
