# Generated by Django 4.0.1 on 2022-02-23 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0019_rename_level_category_mptt_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='mptt_level',
            new_name='level',
        ),
    ]
