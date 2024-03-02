# Generated by Django 5.0.1 on 2024-02-07 04:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('store', models.CharField(max_length=150, verbose_name='Product store name')),
                ('store_city', models.CharField(max_length=50)),
                ('store_country', models.CharField(max_length=50)),
                ('store_contact', models.CharField(max_length=15)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]