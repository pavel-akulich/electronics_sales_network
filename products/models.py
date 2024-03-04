from django.db import models


class Product(models.Model):
    """
    Model class representing a product.

    Attributes:
        name (CharField): The name of the product.
        product_model (CharField): The model of the product.
        date_release (DateField): The date of release of the product.
    """
    name = models.CharField(max_length=255, verbose_name='product name')
    product_model = models.CharField(max_length=150, verbose_name='product model')
    date_release = models.DateField(verbose_name='date of release product')

    def __str__(self):
        """
        Method to return a string representation of the product.

        Returns:
            str: The name of the product.
        """
        return f'{self.name}'

    class Meta:
        """
        Metadata class for the Product model.

        Attributes:
            verbose_name (str): The verbose name of the model.
            verbose_name_plural (str): The plural verbose name of the model.
        """
        verbose_name = 'product'
        verbose_name_plural = 'products'
