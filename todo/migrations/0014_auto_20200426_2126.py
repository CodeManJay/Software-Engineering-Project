# Generated by Django 3.0.3 on 2020-04-26 15:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20200426_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingitem',
            name='due_time',
            field=models.TimeField(default=datetime.datetime(2020, 4, 26, 15, 56, 19, 610835, tzinfo=utc)),
        ),
    ]
