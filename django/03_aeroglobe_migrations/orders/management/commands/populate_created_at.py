from datetime import datetime, timedelta, timezone

from django.core.management.base import BaseCommand
from django.db import transaction
from orders.models import Orders


class Command(BaseCommand):
    help = "Populate created_at column in batches"

    def handle(self, *args, **kwargs):
        now = datetime.now(tz=timezone.utc).strftime("%I:%M:%S %p").lower()
        self.stdout.write(
            self.style.NOTICE(f"Starting populating created_at records {now=}...")
        )
        batch_size = 10000
        now = datetime.now()
        two_days_ago = now - timedelta(days=2)

        # Fetch the total number of rows that need to be updated
        total_rows = Orders.objects.filter(created_at__isnull=True).count()

        for start in range(0, total_rows, batch_size):
            end = start + batch_size

            # Fetch the primary keys in the current batch
            pks = Orders.objects.filter(created_at__isnull=True).values_list(
                "pk", flat=True
            )[start:end]

            # Perform the update using the fetched primary keys
            with transaction.atomic():
                Orders.objects.filter(pk__in=pks).update(created_at=two_days_ago)

            self.stdout.write(f"Updated rows {start} to {end}")

        now = datetime.now(tz=timezone.utc).strftime("%I:%M:%S %p").lower()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated created_at records {now=}.")
        )
