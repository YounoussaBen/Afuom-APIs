from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from backend.models import BaseModel

class Cart(BaseModel):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('created_by', 'product')

    def __str__(self):
        return f"{self.created_by.username}'s Cart"
