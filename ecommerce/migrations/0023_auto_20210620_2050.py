# Generated by Django 3.1.2 on 2021-06-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_auto_20210620_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='other_image',
        ),
        migrations.AddField(
            model_name='product',
            name='other_image_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='other_image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='other_image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='other_image_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
