import random
from datetime import datetime, timedelta, timezone

from django.core.management.base import BaseCommand
from django.db import transaction
from orders.models import Orders


class Command(BaseCommand):
    help = "Populate Orders table with sample data"

    def handle(self, *args, **kwargs):
        batch_size = 10000
        total_records = 5000000
        # total_records = 10
        orders = []

        destinations = [
            "Karachi",
            "Lahore",
            "Islamabad",
            "Peshawar",
            "Quetta",
            "Rawalpindi",
            "Attock",
        ]
        iata_codes = ["KHI", "LHE", "PES", "QUE", "RPI", "ATK"]
        types = ["ONEWAY", "TWOWAY", "RETURN"]
        now = datetime.now(tz=timezone.utc).strftime("%I:%M:%S %p").lower()
        self.stdout.write(
            self.style.NOTICE(f"Starting populating {total_records} records {now=}...")
        )

        def random_date():
            start_date = datetime.now() - timedelta(days=365)
            return start_date + timedelta(days=random.randint(1, 365))

        for _ in range(total_records):
            order = Orders(
                destination=random.choice(destinations),
                destination_iata=random.choice(iata_codes),
                origin=random.choice(destinations),
                origin_iata=random.choice(iata_codes),
                type=random.choice(types),
                departure=random_date(),
                arrival=random_date(),
            )
            orders.append(order)

            if len(orders) % batch_size == 0:
                with transaction.atomic():
                    Orders.objects.bulk_create(orders)
                    orders = []

        if orders:
            with transaction.atomic():
                Orders.objects.bulk_create(orders)

        now = datetime.now(tz=timezone.utc).strftime("%I:%M:%S %p").lower()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully populated {total_records} records {now=}."
            )
        )
