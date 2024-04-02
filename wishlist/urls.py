from django.urls import path
from .views import WishlistListCreateView, WishlistDeleteView

urlpatterns = [
    path('add/', WishlistListCreateView.as_view(), name='wishlist-add'),
    path('remove/<int:pk>/', WishlistDeleteView.as_view(), name='wishlist-remove'),
]
