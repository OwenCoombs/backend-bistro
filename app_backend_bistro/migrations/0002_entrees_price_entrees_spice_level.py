# Generated by Django 5.0.6 on 2024-05-23 14:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend_bistro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrees',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrees',
            name='spice_level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]