# Generated by Django 3.1.5 on 2021-01-18 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Requests', '0008_auto_20210118_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='requests',
            name='wrote_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
