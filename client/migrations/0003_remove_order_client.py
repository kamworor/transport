# Generated by Django 4.2.2 on 2023-06-16 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_order_client_order_vehicles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
    ]
