# Generated by Django 3.0.3 on 2020-06-04 04:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200604_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 4, 4, 30, 15, 518442, tzinfo=utc)),
        ),
    ]
