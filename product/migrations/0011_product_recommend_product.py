# Generated by Django 4.0.1 on 2022-02-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_recommendproduct'),
        ('product', '0010_remove_product_tag_product_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recommend_product',
            field=models.ManyToManyField(related_name='product_recommend', to='category.RecommendProduct'),
        ),
    ]