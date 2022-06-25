# Generated by Django 3.2.4 on 2021-06-15 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('features', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('general', 'General'), ('premium', 'Premium')], max_length=50)),
            ],
        ),
    ]
