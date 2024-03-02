from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=256)
    store = models.CharField(max_length=150, verbose_name="Product store name")
    store_city = models.CharField(max_length=50)
    store_country = models.CharField(max_length=50)
    store_contact = models.CharField(max_length=15)
    created_at = models.DateField(auto_now_add=True)
