from django.contrib import admin

from BarDeAposta.models import Team, Sport, Customer, Product


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cpf_number', 'phone')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


admin.site.register(Team, TeamAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
