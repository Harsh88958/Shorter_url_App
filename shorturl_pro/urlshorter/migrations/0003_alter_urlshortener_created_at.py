# Generated by Django 4.2 on 2023-10-24 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshorter', '0002_alter_urlshortener_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]