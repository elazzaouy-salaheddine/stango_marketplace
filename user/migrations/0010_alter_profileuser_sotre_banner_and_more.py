# Generated by Django 4.0.1 on 2022-02-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_profileuser_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='sotre_banner',
            field=models.ImageField(default='static/default/image.jpg', upload_to='media/uploads/vendors'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='sotre_logo',
            field=models.ImageField(default='static/default/image.jpg', upload_to='media/uploads/vendors'),
        ),
    ]
