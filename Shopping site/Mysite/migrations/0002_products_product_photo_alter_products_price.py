# Generated by Django 5.0.4 on 2024-05-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_photo',
            field=models.ImageField(default='', upload_to='Mysite/images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
    ]