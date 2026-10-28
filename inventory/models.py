from django.db import models


class Supplier(models.Model):

    name = models.CharField(
        max_length=255,
        db_index=True
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(
        max_length=255,
        db_index=True
    )

    sku = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField()

    stock_quantity = models.PositiveIntegerField(
        default=0
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="products"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name