# Generated by Django 4.1.4 on 2024-01-03 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_bookings_bk_time_userpfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='BK_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 3, 13, 11, 1, 536759, tzinfo=datetime.timezone.utc)),
        ),
    ]
