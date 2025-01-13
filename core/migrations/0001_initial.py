# Generated by Django 4.2.17 on 2025-01-13 10:35

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campervan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('location', models.CharField(max_length=100)),
                ('availability_status', models.BooleanField(default=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]