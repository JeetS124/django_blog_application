# Generated by Django 4.2.3 on 2023-07-15 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_post_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_time',
        ),
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 15, 18, 59, 494671)),
        ),
    ]
