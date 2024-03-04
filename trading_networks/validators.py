from rest_framework import serializers


def validate_supplier_for_factory(data):
    """
    Function to validate supplier for a factory network.

    Args:
        data (dict): The data to be validated.

    Returns:
        dict: The validated data.

    Raises:
        serializers.ValidationError: If the network type is Factory and a supplier is provided.
    """
    network_type = data.get('network_type')
    supplier = data.get('supplier')

    if network_type == 'Factory' and supplier:
        raise serializers.ValidationError("You cannot specify a supplier for a Factory type network")
    return data


def validate_network_supplier(data):
    """
    Function to validate levels network supplier.

    Args:
        data (dict): The data to be validated.

    Returns:
        dict: The validated data.

    Raises:
        serializers.ValidationError: If the supplier's network level is already at the maximum.
    """
    supplier = data.get('supplier')
    if supplier and supplier.network_level >= 2:
        raise serializers.ValidationError("The level of the nodes has already reached its maximum 3")
    return data
