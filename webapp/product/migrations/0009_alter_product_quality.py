# Generated by Django 4.0.6 on 2022-07-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_merge_20220731_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quality',
            field=models.IntegerField(choices=[(1, 'very poor'), (2, 'poor'), (3, 'good'), (4, 'very good'), (5, 'excellent')], db_index=True, default=3, verbose_name='품질'),
        ),
    ]