# Generated by Django 3.0.5 on 2021-03-19 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210319_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thubnail',
            new_name='thumbnail',
        ),
    ]
