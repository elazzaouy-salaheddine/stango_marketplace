# Generated by Django 4.0.1 on 2022-03-13 19:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0038_alter_profileuser_watsapp_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]