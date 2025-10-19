from django.db import models
from django.utils import timezone


class Orders(models.Model):
    destination = models.TextField(max_length=150)
    destination_iata = models.TextField(max_length=15)
    origin = models.TextField(max_length=150)
    origin_iata = models.TextField(max_length=15)
    type = models.TextField(max_length=30)
    departure = models.DateField()
    arrival = models.DateField()
