from django.contrib import admin
from .models import Address, Customers, Products

# Register your models here.
class addressAdmin(admin.ModelAdmin):
    list_display = ('adr_id', 'adr_barangay')
    search_fields = ['adr_barangay']

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Address, addressAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cus_id', 'cus_name', 'cus_contact', 'cus_address_id')
    search_fields = ['cus_name']
    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Customers, CustomerAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('prod_id', 'prod_name', 'prod_price')
    search_fields = ['prod_name']
    list_per_page = 10

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Products, ProductsAdmin)