# Generated by Django 3.0.3 on 2020-06-01 06:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200601_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 1, 6, 30, 40, 947927, tzinfo=utc)),
        ),
    ]
