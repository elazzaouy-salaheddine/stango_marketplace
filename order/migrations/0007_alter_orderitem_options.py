# Generated by Django 4.0.1 on 2022-02-10 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_orderitem_options_alter_custemer_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('date_add',)},
        ),
    ]