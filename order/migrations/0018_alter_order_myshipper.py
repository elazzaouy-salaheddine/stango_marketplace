# Generated by Django 4.0.1 on 2022-05-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0044_profileuser_created_profileuser_updated'),
        ('order', '0017_remove_order_myshipper_order_myshipper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='myshipper',
            field=models.ManyToManyField(blank=True, related_name='myshipperuser', to='user.ProfileUser'),
        ),
    ]
