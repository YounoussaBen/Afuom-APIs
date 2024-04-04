from django.urls import path
from .views import CartListCreateView, CartUpdateView, CartDeleteView

urlpatterns = [
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartUpdateView.as_view(), name='cart-update'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart-delete'),
]
