# Generated by Django 2.0.7 on 2018-08-26 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0002_auto_20180825_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='shift_id',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
