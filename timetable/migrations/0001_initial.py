# Generated by Django 2.1 on 2018-09-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=10)),
                ('weather', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=30)),
                ('t1000', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1030', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1100', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1130', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1200', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1230', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1300', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1330', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1400', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1430', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1500', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1530', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1600', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1630', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1700', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1730', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1800', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1830', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1900', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('t1930', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'timetables',
            },
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together={('day', 'weather', 'place')},
        ),
    ]
