# Generated by Django 4.0.1 on 2022-02-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_alter_profileuser_sotre_banner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='Refund_Policy',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='Return_Policy',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='Shipping_Policy',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='description',
            field=models.TextField(),
        ),
    ]
