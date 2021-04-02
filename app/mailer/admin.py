#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Company, Contact, Order

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'bic']

admin.site.register(Company, CompanyAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['company', 'first_name', 'last_name', 'email']

admin.site.register(Contact, ContactAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'company', 'contact', 'order_date']

admin.site.register(Order, OrderAdmin)