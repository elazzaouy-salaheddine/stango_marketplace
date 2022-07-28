# Generated by Django 4.0.1 on 2022-04-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_payment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Call_Center_status',
            field=models.CharField(choices=[('No Reply', 'No Reply'), ('Confirmed', 'Confirmed'), ('Canceled', 'Canceled'), ('Unknown', 'Unknown')], default='Unknown', max_length=10),
        ),
    ]