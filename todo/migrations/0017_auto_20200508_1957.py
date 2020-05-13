# Generated by Django 3.0.3 on 2020-05-08 14:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0016_auto_20200508_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='contact',
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='author_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetingitem',
            name='due_time',
            field=models.TimeField(default=datetime.datetime(2020, 5, 8, 14, 27, 25, 936306, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
