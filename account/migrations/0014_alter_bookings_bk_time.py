# Generated by Django 4.1.4 on 2024-01-03 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_bookings_bk_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='BK_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 3, 13, 16, 59, 922973, tzinfo=datetime.timezone.utc)),
        ),
    ]