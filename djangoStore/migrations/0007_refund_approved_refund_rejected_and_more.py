# Generated by Django 5.0 on 2024-01-14 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoStore', '0006_alter_purchaseprocess_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='refund',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_amount',
            field=models.FloatField(default=0, verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_discription',
            field=models.CharField(max_length=250, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='img/', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(default=0, verbose_name='Cost'),
        ),
    ]
