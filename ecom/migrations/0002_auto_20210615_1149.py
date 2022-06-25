# Generated by Django 3.2.4 on 2021-06-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='ecom/theme_image')),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='PricingPort',
            new_name='PortfolioPricing',
        ),
    ]
