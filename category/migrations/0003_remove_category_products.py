# Generated by Django 4.0.1 on 2022-01-23 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_posts_category_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
    ]
