# Generated by Django 3.0.5 on 2021-03-13 06:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.TimeField(verbose_name=datetime.datetime(2021, 3, 13, 6, 51, 20, 597281, tzinfo=utc)),
        ),
    ]
