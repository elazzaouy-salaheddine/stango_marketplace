# Generated by Django 4.0.1 on 2022-02-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_alter_profileuser_sotre_banner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='sotre_banner',
            field=models.ImageField(default='default/1.jpg', upload_to='media/uploads/vendors'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='sotre_logo',
            field=models.ImageField(default='default/1.jpg', upload_to='media/uploads/vendors'),
        ),
    ]
