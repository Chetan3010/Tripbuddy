# Generated by Django 4.1.4 on 2024-01-02 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_bookings_bk_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='BK_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 12, 26, 53, 804390, tzinfo=datetime.timezone.utc)),
        ),
    ]
