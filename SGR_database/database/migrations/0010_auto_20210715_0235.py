# Generated by Django 3.2.4 on 2021-07-15 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_alter_statement_statement_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to='database.industry'),
        ),
        migrations.AlterField(
            model_name='industrylevel1',
            name='industry_level_1',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='stockexchange',
            name='stock_exchange',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AddConstraint(
            model_name='statementrow',
            constraint=models.UniqueConstraint(fields=('statement', 'row_order'), name='unique_row'),
        ),
    ]
