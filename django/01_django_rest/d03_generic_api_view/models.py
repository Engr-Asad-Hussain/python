from django.db import models
from django.utils import timezone


class Reviews(models.Model):
    comment = models.CharField(max_length=255)
    author = models.CharField(
        max_length=150, verbose_name="Person who create a comment."
    )
    up_votes = models.PositiveIntegerField(
        default=0, verbose_name="Number of up-votes for a comment."
    )
    created_at = models.DateTimeField(default=timezone.now)
