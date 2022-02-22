# Generated by Django 4.0.1 on 2022-02-20 20:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0013_alter_brand_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='format: not required', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='category.category', verbose_name='parent of category'),
        ),
        migrations.AddField(
            model_name='category',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
    ]