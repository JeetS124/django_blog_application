# Generated by Django 5.0.6 on 2024-06-13 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 13, 23, 14, 47, 364893)),
        ),
    ]
