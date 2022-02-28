# Generated by Django 4.0.1 on 2022-02-28 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_alter_comment_options_remove_comment_created_and_more'),
        ('product', '0031_alter_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='comment.comment'),
            preserve_default=False,
        ),
    ]
