# Generated by Django 4.2.3 on 2023-07-15 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='post_image.jpg', upload_to='upload_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 15, 11, 39, 39, 588101)),
        ),
    ]
