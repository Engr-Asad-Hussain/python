## aeroglobe-migration
------------
A Django Migration Service

## Setup local development
1. Clone the repository
```sh
git clone https://github.com/Engr-Asad-Hussain/aeroglobe-migrations.git && cd aeroglobe-migrations
```

2. Create a virtual environment (for Linux distribution) and activate virtual environment.
```sh
python -m virtualenv venv && . venv/bin/activate
```

3. Install dependencies
```sh
pip install -r requirements.txt
```

4. Setup database
```sh
docker-compose -f docker-compose.db.yaml up -d
```

5. Create a `.env` file in the root of the project and inject following variables:
```sh
# Database Configurations
DATABASE_NAME="postgres-django-migrations"
DATABASE_USER="postgres"
DATABASE_PASSWORD="admin123"
DATABASE_HOST="localhost"
DATABASE_POST="5432"
```

6. Apply initial migrations
```sh
python manage.py makemigrations && python manage.py migrate
```

7. Populate database with 5 million records
```sh
python manage.py populate_orders
```

8. Modify the `orders.models.py` file to include the `created_at` datetime field i.e.,
```py
from django.utils import timezone
from django.db import models


class Orders(models.Model):
    destination = models.TextField(max_length=150)
    destination_iata = models.TextField(max_length=15)
    origin = models.TextField(max_length=150)
    origin_iata = models.TextField(max_length=15)
    type = models.TextField(max_length=30)
    departure = models.DateField()
    arrival = models.DateField()
    created_at = models.DateTimeField(null=True)

```

9. Apply migrations again
```sh
python manage.py makemigrations && python manage.py migrate
```

10. Add the `created_at` values in the database.
```sh
python manage.py populate_created_at
```

11. Cleanup resources
```sh
docker-compose -f docker-compose.db.yaml down -v
```