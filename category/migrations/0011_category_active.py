# Generated by Django 4.0.1 on 2022-02-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0010_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
