# Generated by Django 4.0.1 on 2022-02-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_profileuser_store_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='store_name',
            field=models.CharField(blank=True, error_messages={'unique': 'The store must be unique '}, max_length=100, unique=True),
        ),
    ]
