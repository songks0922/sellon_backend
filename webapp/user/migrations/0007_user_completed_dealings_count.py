# Generated by Django 4.1 on 2022-08-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='completed_dealings_count',
            field=models.PositiveIntegerField(default=0, verbose_name='거래횟수'),
        ),
    ]