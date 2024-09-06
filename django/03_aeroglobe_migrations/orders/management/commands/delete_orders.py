from datetime import datetime, timezone
from django.core.management.base import BaseCommand
from orders.models import Orders


class Command(BaseCommand):
    help = "Delete all records from Orders table"

    def handle(self, *args, **kwargs):
        now = datetime.now(tz=timezone.utc).strftime("%I:%M:%S %p").lower()
        self.stdout.write(self.style.NOTICE(f"Starting deleting records {now=}..."))

        total_records = Orders.objects.count()
        Orders.objects.all().delete()

        now = datetime.now(tz=timezone.utc).strftime("%I:%M:%S %p").lower()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully deleted {total_records} records {now=}.")
        )
