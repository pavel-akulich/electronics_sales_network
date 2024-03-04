from django.db import models

from products.models import Product
from users.models import NULLABLE


class Network(models.Model):
    """
    Model class representing a network.

    Attributes:
        NETWORK_CHOICES (tuple): Choices for the network_type field.
        network_type (CharField): The type of the network.
        network_level (IntegerField): The level of the network in the hierarchy.
        name (CharField): The name of the network.
        email (EmailField): The email of the network.
        country (CharField): The country of the network.
        city (CharField): The city of the network.
        street (CharField): The street of the network.
        house_number (CharField): The house number of the network.
        products (ManyToManyField): The products associated with the network.
        supplier (ForeignKey): The supplier network.
        debt (DecimalField): The debt of the network.
        created_at (DateTimeField): The date of creation of the network.
    """
    NETWORK_CHOICES = (
        ('Factory', 'Factory'),
        ('RetailNetwork', 'RetailNetwork'),
        ('IndividualBusinessman', 'IndividualBusinessman')
    )

    network_type = models.CharField(max_length=35, choices=NETWORK_CHOICES, verbose_name='network type')
    network_level = models.IntegerField(default=0, verbose_name='level in the hierarchy')
    name = models.CharField(max_length=150, verbose_name='network name')
    email = models.EmailField(verbose_name='email of the network')
    country = models.CharField(max_length=80, verbose_name='country')
    city = models.CharField(max_length=80, verbose_name='city')
    street = models.CharField(max_length=80, verbose_name='street')
    house_number = models.CharField(max_length=30, verbose_name='house number')
    products = models.ManyToManyField(Product, verbose_name='product')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='supplier', **NULLABLE)
    debt = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='debt')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date of creation')

    def __str__(self):
        """
        Method to return a string representation of the network.

        Returns:
            str: The string representation of the network.
        """
        return f'{self.network_type} - {self.name}, level in the hierarchy - {self.network_level}'

    class Meta:
        """
        Metadata class for the Network model.

        Attributes:
            verbose_name (str): The verbose name of the model.
            verbose_name_plural (str): The plural verbose name of the model.
        """
        verbose_name = 'network'
        verbose_name_plural = 'networks'
