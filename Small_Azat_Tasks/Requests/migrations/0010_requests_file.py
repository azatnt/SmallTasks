# Generated by Django 3.1.5 on 2021-01-18 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0009_auto_20210118_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='file',
            field=models.FileField(blank=True, upload_to='files'),
        ),
    ]
