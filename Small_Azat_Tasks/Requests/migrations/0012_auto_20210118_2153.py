# Generated by Django 3.1.5 on 2021-01-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0011_auto_20210118_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='file',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]
