# Generated by Django 4.0.1 on 2022-01-26 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_remove_category_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_logo',
            field=models.ImageField(default=1, height_field=190, upload_to='media/uploads/categores', width_field=184),
            preserve_default=False,
        ),
    ]
