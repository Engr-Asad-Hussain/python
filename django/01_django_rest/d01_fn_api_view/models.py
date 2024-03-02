from django.db import models
from django.utils import timezone


class Products(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.PositiveIntegerField()
    seller = models.CharField(max_length=150, verbose_name="Seller name of a product")
    seller_city = models.CharField(max_length=50, verbose_name="City of a seller")
    seller_country = models.CharField(max_length=50, verbose_name="Country of a seller")
    seller_contact = models.CharField(
        max_length=15, verbose_name="Contact number of a seller"
    )
    created_at = models.DateTimeField(default=timezone.now)
