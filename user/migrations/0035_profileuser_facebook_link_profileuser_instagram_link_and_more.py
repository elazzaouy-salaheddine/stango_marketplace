# Generated by Django 4.0.1 on 2022-02-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_alter_profileuser_refund_policy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='watsapp_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]