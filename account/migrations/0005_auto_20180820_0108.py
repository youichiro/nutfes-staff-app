# Generated by Django 2.0.7 on 2018-08-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='有効なユーザとして扱うかを指定する.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='ユーザが管理サイトにアクセスできるかを指定する.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(help_text='学生番号を入力してください. (ex. s0000000)', max_length=7, unique=True),
        ),
    ]
