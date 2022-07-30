# Generated by Django 4.0.6 on 2022-07-30 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='추가된 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 일시')),
                ('file', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uploader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Imaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='추가된 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 일시')),
                ('imageable_id', models.PositiveIntegerField(null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='file_manager.image')),
                ('imageable_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Imaging',
                'verbose_name_plural': 'Imagings',
                'db_table': 'imagings',
            },
        ),
    ]