from django.contrib.auth.models import User
from backend.models import BaseModel
from django.db import models
from django.db.models import Q

class CategoryManager(models.Manager):
    def get_categories(self):
        return self.filter()
class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    objects = CategoryManager()

    def __str__(self):
        return self.name

class ProductManager(models.Manager):
    def search_products(self, search_query):
        return self.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField(blank=True)
    stock = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attributes = models.JSONField(default=dict)

    objects = ProductManager()

    def __str__(self):
        return self.name
