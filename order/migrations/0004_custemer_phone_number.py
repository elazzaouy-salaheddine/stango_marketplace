# Generated by Django 4.0.1 on 2022-02-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_custemer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='custemer',
            name='phone_number',
            field=models.CharField(default='02365988', max_length=255),
        ),
    ]
