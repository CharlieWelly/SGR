# Generated by Django 3.2.4 on 2021-07-02 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_company_exchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='exchange',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to='database.stockexchange'),
        ),
        migrations.AddConstraint(
            model_name='company',
            constraint=models.UniqueConstraint(fields=('code_vs', 'name'), name='unique_company'),
        ),
    ]