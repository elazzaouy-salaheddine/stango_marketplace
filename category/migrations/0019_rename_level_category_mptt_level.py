# Generated by Django 4.0.1 on 2022-02-23 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0018_category_level_category_lft_category_rght_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='level',
            new_name='mptt_level',
        ),
    ]