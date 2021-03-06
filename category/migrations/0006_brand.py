# Generated by Django 4.0.1 on 2022-01-26 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_category_category_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='media/uploads/brands')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
