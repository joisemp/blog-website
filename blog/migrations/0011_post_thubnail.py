# Generated by Django 3.0.5 on 2021-03-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210318_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thubnail',
            field=models.ImageField(blank=True, null=True, upload_to='Public/images/thubnail'),
        ),
    ]
