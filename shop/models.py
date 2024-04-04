from django.contrib.auth.models import User
from backend.models import BaseModel
from django.db import models
class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField(blank=True)
    stock = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attributes = models.JSONField(default=dict)
    def __str__(self):
        return self.name
