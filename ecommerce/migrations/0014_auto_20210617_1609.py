# Generated by Django 3.1.2 on 2021-06-17 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_auto_20210617_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completedtransaction',
            old_name='message',
            new_name='tracking_id',
        ),
        migrations.RemoveField(
            model_name='completedtransaction',
            name='customer',
        ),
    ]
