# Generated by Django 4.0.1 on 2022-01-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_vendor'),
        ('user', '0004_profileuser_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='product',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='product',
            field=models.ManyToManyField(related_name='vendor_products', to='product.Product'),
        ),
    ]
