from django.db import models

# Create your models here.
from django.db import models

# Product model to store product information
class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name
    description = models.TextField()  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    stock = models.PositiveIntegerField()  # Product stock
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Product image

    def __str__(self):
        return self.name  # Display product name in admin panel
