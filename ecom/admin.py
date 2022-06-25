from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'delivary_mail', 'country']



@admin.register(PortfolioPricing)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'package_name', 'price', 'category']

@admin.register(PortfolioTheme)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image']


@admin.register(OrderPortfolio)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'price', 'theme', 'status', 'ordered_date',
    'domain_name', 'buy_domain']