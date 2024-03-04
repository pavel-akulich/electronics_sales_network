from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing Product model instances.

    Attributes:
        Meta (class): Nested class containing metadata for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized representation.
    """

    class Meta:
        """
        Metadata class for the ProductSerializer.

        Attributes:
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized representation.
        """
        model = Product
        fields = ('pk', 'name', 'product_model', 'date_release',)
