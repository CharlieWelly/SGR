# Generated by Django 3.2.4 on 2021-07-15 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20210715_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='statement_categories',
            field=models.CharField(choices=[('DN', 'Doanh nghiệp'), ('CK', 'Chứng Khoán'), ('QLQ', 'Quản lý quỹ'), ('TC', 'Công ty tài chính')], default='DN', max_length=3),
        ),
        migrations.AlterField(
            model_name='statement',
            name='statement_name',
            field=models.CharField(max_length=100),
        ),
    ]
