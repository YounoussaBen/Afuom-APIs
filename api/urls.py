from django.urls import include, path

urlpatterns = [
    path("auth/", include("authentication.urls")),
    path("shop/", include("shop.urls")),
    path("wishlist/", include("wishlist.urls")),
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),
]
