# Generated by Django 4.0.1 on 2022-05-06 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_order_call_center_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Shipping_status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Return', 'Return'), ('Unknown', 'Unknown')], default='Unknown', max_length=10),
        ),
    ]
