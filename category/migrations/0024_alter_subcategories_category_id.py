# Generated by Django 4.0.1 on 2022-02-25 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0023_alter_subcategories_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategories',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='category.category'),
        ),
    ]
