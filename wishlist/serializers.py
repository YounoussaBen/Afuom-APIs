from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        read_only_fields = ("created", "updated")
        exclude = ("is_deleted",)
