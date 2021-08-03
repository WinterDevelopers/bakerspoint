# Generated by Django 3.1.2 on 2021-07-27 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0025_auto_20210719_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ManyToManyField(null=True, to='ecommerce.Product'),
        ),
    ]