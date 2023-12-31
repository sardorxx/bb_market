# Generated by Django 5.0 on 2023-12-15 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comments_image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_guid',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketface.type'),
        ),
    ]
