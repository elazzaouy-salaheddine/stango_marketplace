# Generated by Django 4.0.1 on 2022-05-07 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_ordershipper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordershipper',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order'),
        ),
    ]