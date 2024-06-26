# Generated by Django 5.0.6 on 2024-05-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend_bistro', '0003_alter_entrees_name_alter_entrees_spice_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('spice_level', models.IntegerField(default=0)),
            ],
        ),
    ]
