from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from trading_networks.models import Network
from users.models import User


class NetworkTestCase(APITestCase):
    """
    Test case class for testing network API endpoints.
    """

    def setUp(self):
        """
        Method to set up the test case.

        Creates a superuser and authenticates the client.
        """
        self.user = User.objects.create(
            email='test_network@gmail.com',
            password='test_network'
        )
        self.user.is_superuser = True
        self.user.is_active = True
        self.user.is_staff = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_network(self):
        """
        Method to test creating a new network instance.
        """
        product = Product.objects.create(
            name='product_1',
            product_model='product_1',
            date_release='2023-09-10'
        )

        data = {
            "network_type": "Factory",
            "name": "test Factory",
            "email": "test@mail.ru",
            "country": "Itest",
            "city": "test",
            "street": "test",
            "house_number": "test",
            "products": [product.pk],
            "debt": 0
        }

        response = self.client.post(
            '/networks/network/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        created_at = response.json()["created_at"]

        self.assertEqual(
            response.json(),
            {
                "pk": 1,
                "network_type": "Factory",
                "network_level": 0,
                "name": "test Factory",
                "email": "test@mail.ru",
                "country": "Itest",
                "city": "test",
                "street": "test",
                "house_number": "test",
                "products": [product.pk],
                "supplier": None,
                "debt": "0.00",
                "created_at": created_at
            }
        )

    def test_list_network(self):
        """
        Method to test listing all networks.
        """
        product = Product.objects.create(
            name='product_1',
            product_model='product_1',
            date_release='2023-09-10'
        )

        network = Network.objects.create(
            network_type='Factory',
            name="test Factory",
            email="test@mail.ru",
            country="Itest",
            city="test",
            street="test",
            house_number="test",
            debt=0
        )

        network.products.add(product)

        response = self.client.get('/networks/network/list/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        created_at = response.json()["results"][0]["created_at"]

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "pk": network.pk,
                        "network_type": "Factory",
                        "network_level": 0,
                        "name": "test Factory",
                        "email": "test@mail.ru",
                        "country": "Itest",
                        "city": "test",
                        "street": "test",
                        "house_number": "test",
                        "products": [product.pk],
                        "supplier": None,
                        "debt": "0.00",
                        "created_at": created_at
                    }
                ]
            }
        )

    def test_detail_network(self):
        """
        Method to test retrieving a single network detail.
        """
        product = Product.objects.create(
            name='product_1',
            product_model='product_1',
            date_release='2023-09-10'
        )

        network = Network.objects.create(
            network_type='Factory',
            name="test Factory",
            email="test@mail.ru",
            country="Itest",
            city="test",
            street="test",
            house_number="test",
            debt=0
        )

        network.products.add(product)

        response = self.client.get(f'/networks/network/detail/{network.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "pk": network.pk,
                "network_type": "Factory",
                "network_level": 0,
                "name": "test Factory",
                "email": "test@mail.ru",
                "country": "Itest",
                "city": "test",
                "street": "test",
                "house_number": "test",
                "products": [product.pk],
                "supplier": None,
                "debt": "0.00",
                "created_at": response.json()["created_at"]
            }
        )

    def test_delete_network(self):
        """
        Method to test deleting a network.
        """
        network = Network.objects.create(
            network_type='Factory',
            name="test Factory",
            email="test@mail.ru",
            country="Itest",
            city="test",
            street="test",
            house_number="test",
            debt=0
        )

        response = self.client.delete(f'/networks/network/delete/{network.pk}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
