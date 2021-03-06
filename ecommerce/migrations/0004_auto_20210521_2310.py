# Generated by Django 3.1.2 on 2021-05-21 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20210507_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
