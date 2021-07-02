# Generated by Django 3.2.4 on 2021-07-01 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_stockexchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='exchange',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to='database.stockexchange'),
        ),
    ]
