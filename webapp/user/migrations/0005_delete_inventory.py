# Generated by Django 4.0.6 on 2022-08-04 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]