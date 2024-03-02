from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
