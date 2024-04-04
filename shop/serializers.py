from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = ("created", "updated")
        exclude = ("is_deleted",)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = ("created", "updated", "created_by")
        exclude = ("is_deleted",)
        
    def create(self, validated_data):
        # Get the user who is creating the product
        user = self.context['request'].user if 'request' in self.context else None

        # Set the created_by field with the user
        validated_data['created_by'] = user

        return super().create(validated_data)