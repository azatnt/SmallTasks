# Generated by Django 3.1.5 on 2021-01-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0006_auto_20210118_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
