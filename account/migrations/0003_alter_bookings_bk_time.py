# Generated by Django 4.1.4 on 2024-01-01 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_bookings_bk_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='BK_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 1, 12, 39, 47, 207954, tzinfo=datetime.timezone.utc)),
        ),
    ]