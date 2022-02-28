# Generated by Django 4.0.1 on 2022-02-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0036_alter_profileuser_facebook_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='instagram_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='twitter_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='watsapp_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
