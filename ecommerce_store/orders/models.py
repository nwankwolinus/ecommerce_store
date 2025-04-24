from django.db import models

# Create your models here.
from django.db import models
from products.models import Product
from users.models import CustomUser

# Order model to store order information
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link order to user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link order to product
    quantity = models.PositiveIntegerField()  # Quantity of product in order
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price of order
    order_date = models.DateTimeField(auto_now_add=True)  # Timestamp when order is placed

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price  # Calculate total price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.user}"  # Display order ID and user in admin panel
