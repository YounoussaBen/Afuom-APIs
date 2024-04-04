from django.urls import path
from .views import CheckoutView, OrderDetailView, UserOrderHistoryView, SellerOrderHistoryView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('user-order-history/', UserOrderHistoryView.as_view(), name='user-order-history'),
    path('seller-order-history/', SellerOrderHistoryView.as_view(), name='seller-order-history'),
]
