# Generated by Django 3.2.4 on 2021-06-22 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_orderportfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderportfolio',
            name='buy_domain',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderportfolio',
            name='domain_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
