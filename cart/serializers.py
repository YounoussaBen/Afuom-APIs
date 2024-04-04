from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        read_only_fields = ("created", "updated", "created_by")
        exclude = ("is_deleted",)
