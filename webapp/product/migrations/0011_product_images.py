# Generated by Django 4.0.6 on 2022-08-03 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0002_productimage_delete_imaging'),
        ('product', '0010_alter_product_quality'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='product_images', through='file_manager.ProductImage', to='file_manager.image'),
        ),
    ]