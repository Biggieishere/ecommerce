# Generated by Django 5.0.4 on 2024-05-24 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0002_products_product_photo_alter_products_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
