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