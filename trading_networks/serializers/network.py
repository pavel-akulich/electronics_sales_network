from rest_framework import serializers

from trading_networks.models import Network
from trading_networks.validators import validate_network_supplier, validate_supplier_for_factory


class NetworkSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing and validating Network model instances.

    This serializer performs custom validation and logic for creating network instances.

    Methods:
        validate: Custom method for validating the serializer data.
        create: Custom method for creating a new network instance.

    Attributes:
        Meta (class): Nested class containing metadata for the serializer.
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized representation.
            read_only_fields (tuple): The read-only fields in the serialized representation.
    """

    def validate(self, data):
        """
        Method to validate the serializer data.

        This method performs custom validation by calling other validation functions.

        Args:
            data (dict): The data to be validated.

        Returns:
            dict: The validated data.

        Note:
            This method calls two custom validation functions: validate_supplier_for_factory
            and validate_network_supplier.
        """
        data = validate_supplier_for_factory(data)
        data = validate_network_supplier(data)
        return data

    def create(self, validated_data):
        """
        Method to create a new network instance.

        This method overrides the default create behavior to set the network_level
        based on the network_type and supplier.

        Args:
            validated_data (dict): The validated data for creating the network.

        Returns:
            Network: The newly created network instance.

        Note:
            The network_level is automatically set based on the network_type and supplier.
        """
        network_type = validated_data['network_type']
        if network_type == 'Factory':
            validated_data['network_level'] = 0
        elif network_type in ['RetailNetwork', 'IndividualBusinessman']:
            supplier = validated_data.get('supplier')
            if supplier:
                validated_data['network_level'] = supplier.network_level + 1
            else:
                validated_data['network_level'] = 1
        return super().create(validated_data)

    class Meta:
        """
        Metadata class for the NetworkSerializer.

        Attributes:
            model (Model): The model class to be serialized.
            fields (tuple): The fields to include in the serialized representation.
            read_only_fields (tuple): The read-only fields in the serialized representation.
        """
        model = Network
        fields = (
            'pk', 'network_type', 'network_level', 'name', 'email', 'country', 'city', 'street', 'house_number',
            'products', 'supplier', 'debt', 'created_at',)
        read_only_fields = ('network_level',)
