# Generated by Django 3.2.4 on 2021-07-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20210702_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='statement_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
