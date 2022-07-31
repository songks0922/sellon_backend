# Generated by Django 4.0.6 on 2022-07-30 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_quality'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='추가된 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정된 일시')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='삭제된 일시')),
                ('name', models.CharField(max_length=100, verbose_name='카테고리 명')),
                ('primary', models.BooleanField(default=False, verbose_name='메인 상품 여부')),
                ('display_order', models.IntegerField(verbose_name='전시 순서')),
            ],
            options={
                'verbose_name': 'ProductCategory',
                'verbose_name_plural': 'ProductCategories',
                'db_table': 'product_categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productcategory', verbose_name='물품 카테고리'),
        ),
    ]