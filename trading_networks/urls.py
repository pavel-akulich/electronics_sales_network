from django.urls import path

from trading_networks.api_views.network import NetworkCreateAPIView, NetworkListAPIView, NetworkRetrieveAPIView, \
    NetworkUpdateAPIView, NetworkDestroyAPIView
from trading_networks.apps import TradingNetworksConfig

app_name = TradingNetworksConfig.name

urlpatterns = [
    path('network/create/', NetworkCreateAPIView.as_view(), name='network-create'),
    path('network/list/', NetworkListAPIView.as_view(), name='network-list'),
    path('network/detail/<int:pk>/', NetworkRetrieveAPIView.as_view(), name='network-detail'),
    path('network/update/<int:pk>/', NetworkUpdateAPIView.as_view(), name='network-update'),
    path('network/delete/<int:pk>/', NetworkDestroyAPIView.as_view(), name='network-delete'),
]
