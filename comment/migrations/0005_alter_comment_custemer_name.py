# Generated by Django 4.0.1 on 2022-02-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_comment_custemer_email_comment_custemer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='custemer_name',
            field=models.CharField(max_length=255),
        ),
    ]
