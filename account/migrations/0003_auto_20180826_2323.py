# Generated by Django 2.0.7 on 2018-08-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180826_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
