# Generated by Django 4.0.1 on 2022-02-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_brand_tag_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]