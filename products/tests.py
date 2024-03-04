from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from users.models import User


class ProductTestCase(APITestCase):
    """
    Test case class for testing product API endpoints.

    Attributes:
        user (User): The user object used for authentication.
    """

    def setUp(self):
        """
        Method to set up the test case.

        Creates a superuser and authenticates the client.
        """
        self.user = User.objects.create(
            email='test@gmail.com',
            password='test'
        )
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.is_staff = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_product(self):
        """
        Method to test creating a new product.
        """
        data = {
            'name': 'test for product create',
            'product_model': 'test for create',
            'date_release': '2023-09-10'
        }

        response = self.client.post(
            '/products/product/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'pk': 1,
                'name': 'test for product create',
                'product_model': 'test for create',
                'date_release': '2023-09-10'
            }
        )

    def test_list_product(self):
        """
        Method to test listing all products.
        """
        product = Product.objects.create(
            name='list product test',
            product_model='list product test',
            date_release='2023-09-10'
        )

        response = self.client.get(
            '/products/product/list/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {'pk': product.pk,
                     'name': 'list product test',
                     'product_model': 'list product test',
                     'date_release': '2023-09-10'
                     }
                ]
            }
        )

    def test_detail_product(self):
        """
        Method to test retrieving a single product detail.
        """
        product = Product.objects.create(
            name='detail product test',
            product_model='detail product test',
            date_release='2023-09-10'
        )

        response = self.client.get(f'/products/product/detail/{product.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': product.pk,
                'name': 'detail product test',
                'product_model': 'detail product test',
                'date_release': '2023-09-10'
            }
        )

    def test_update_product(self):
        """
        Method to test updating a product.
        """
        product = Product.objects.create(
            name='product test',
            product_model='product test',
            date_release='2023-09-10'
        )

        updated_data = {
            'name': 'update product test',
            'product_model': 'update product test',
            'date_release': '2023-09-10'
        }

        response = self.client.put(
            f'/products/product/update/{product.pk}/',
            data=updated_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'pk': product.pk,
                'name': 'update product test',
                'product_model': 'update product test',
                'date_release': '2023-09-10'
            }
        )

    def test_delete_product(self):
        """
        Method to test deleting a product.
        """
        product = Product.objects.create(
            name='delete product test',
            product_model='delete product test',
            date_release='2023-09-10'
        )

        response = self.client.delete(
            f'/products/product/delete/{product.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
