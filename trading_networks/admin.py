from django.contrib import admin, messages

from trading_networks.models import Network


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """
    Admin class for managing Network model instances in the Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
        list_display_links (tuple): The fields to use as links in the admin list view.
        readonly_fields (tuple): The fields to display as read-only in the admin interface.
        list_filter (tuple): The fields to use for filtering in the admin interface.
        actions (list): The custom actions available in the admin interface.
    """
    list_display = (
        'pk', 'network_type', 'network_level', 'name', 'email', 'country', 'city', 'street', 'house_number', 'supplier',
        'debt',)
    list_display_links = ('pk', 'supplier',)
    readonly_fields = ('network_type', 'network_level',)
    list_filter = ('city',)

    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """
        Custom admin action to clear debt for selected network instances.

        Args:
            request (HttpRequest): The HTTP request object.
            queryset (QuerySet): The queryset containing selected network instances.

        Note:
            This action sets the debt field to 0 for the selected network instances
            and displays a success message in the admin interface.
        """
        updated = queryset.update(debt=0)
        self.message_user(request, f'The debt has been cleared from {updated} objects.', messages.SUCCESS)
