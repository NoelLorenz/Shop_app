from django.contrib import admin
from django.db import models
from .models import Orders
from .models import Orderitems


# Register your models here.
class ItemsModelInline(admin.TabularInline):
    model = Orderitems
    extra = 1
    # raw_id_fields = ('oi_buyer',)
    # autocomplete_fields = ['oi_buyer']

class ChildModelAdmin(admin.ModelAdmin):
    search_fields = ['oi_id']
    list_display = ('oi_id', 'oi_buyer', 'oi_type', 'oi_size', 'oi_qty','oi_date', 'oi_status', 'oi_price')

class orderAdmin(admin.ModelAdmin):
    list_display = ('order_id','order_buyer_id', 'order_buyer_adrs', 'orderpay_method')
    search_fields = ['order_id']
    list_per_page = 10
    inlines = [ItemsModelInline]

    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Orders, orderAdmin)