# Generated by Django 3.1.4 on 2021-01-31 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0008_auto_20210131_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 31, 10, 53, 12, 534888, tzinfo=utc)),
        ),
    ]
