from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from backend.models import BaseModel


class ShippingAddress(BaseModel):
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"Shipping Address"

class Order(BaseModel):
    PENDING = 'Pending'
    FULFILLED = 'Fulfilled'
    CANCELED = "Canceled"
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (FULFILLED, 'Fulfilled'),
        (CANCELED, 'Canceled'),

    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.created_by.username}"
    
class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"
