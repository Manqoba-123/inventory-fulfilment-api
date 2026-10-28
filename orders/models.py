from django.db import models
from django.conf import settings
from inventory.models import Product


class FulfilmentOrder(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered")
    )

    customer_name = models.CharField(
        max_length=255
    )

    customer_email = models.EmailField()

    products = models.ManyToManyField(
        Product
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id}"