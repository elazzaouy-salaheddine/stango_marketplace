# Generated by Django 4.0.1 on 2022-04-28 22:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0041_alter_profileuser_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='shippers',
            field=models.ManyToManyField(blank=True, related_name='shippers', to=settings.AUTH_USER_MODEL),
        ),
    ]
