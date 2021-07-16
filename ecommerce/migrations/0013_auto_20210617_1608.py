# Generated by Django 3.1.2 on 2021-06-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_completedtransaction_tracking_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedtransaction',
            name='tracking_id',
        ),
        migrations.AddField(
            model_name='completedtransaction',
            name='message',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
