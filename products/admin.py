from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin class for managing Product model instances in the Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
    """
    list_display = ('pk', 'name', 'product_model', 'date_release',)
