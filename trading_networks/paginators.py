from rest_framework.pagination import PageNumberPagination


class NetworkPaginator(PageNumberPagination):
    """
    Paginator class for paginating Network objects.

    Attributes:
        page_size (int): The default number of items per page.
        page_size_query_param (str): The query parameter to control the page size.
        max_page_size (int): The maximum allowed page size.
    """
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 30
