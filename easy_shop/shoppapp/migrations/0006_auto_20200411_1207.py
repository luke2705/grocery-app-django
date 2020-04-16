# Generated by Django 3.0.5 on 2020-04-11 17:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shoppapp', '0005_auto_20200411_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 17, 7, 23, 622318, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]