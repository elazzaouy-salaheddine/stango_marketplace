# Generated by Django 4.0.1 on 2022-01-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]
