from django.db import models
import uuid
from django.db.models import AutoField
import datetime
from libraries.models import Address, Customers, Products


# Create your models here.



class Odr(models.Model):
    DEL_STATUS = [
        (1, 'Delivered'),
        (2, 'Not Delivered'),
    ]

    PAY_METHOD = [
        (1, 'Cash'),
        (2, 'Gcash'),
        (3, 'PayPal'),
    ]

    order_id = models.AutoField(db_column='order_id', primary_key=True, editable=False)
    # order_no = models.IntegerField(db_column='order_no', default=0)
    order_buyer_id = models.ForeignKey(Customers, db_column='buyer_id', on_delete=models.CASCADE, default=1)
    order_buyer_adrs = models.IntegerField(db_column='order_buyer_adrs', choices=Address.BARANGAY, default='')
    order_date = models.DateTimeField(db_column='order_date', blank=True, null=True, auto_now_add=True)
    # oderdel_status =  models.IntegerField(db_column='orderdel_status', choices=DEL_STATUS, default=2)
    orderpay_method =  models.IntegerField(db_column='orderpay_method', choices=PAY_METHOD, default=1)

    def __str__(self):
        return str(self.order_buyer_id)
    
    def save(self, *args, **kwargs):
        if self.order_buyer_id:
            self.order_buyer_adrs = self.order_buyer_id.cus_address_id

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'tbl_order'
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'


class Orderitems(models.Model):

    OITEM_SIZE =[
        (1, 'Small'),
        (2, 'Medium'),
        (3, 'Large'),
        (4, 'Extra-Large'),
    ]

    oi_id = models.AutoField(db_column='oi_id', primary_key=True, editable=False)
    oi_order = models.ForeignKey(Odr, db_column='oi_order_id', on_delete=models.CASCADE, null=False, blank=False, default='')
    oi_type = models.ForeignKey(Products, db_column='oi_type', on_delete=models.CASCADE, default=None,  related_name='orderitems_by_name')
    oi_size = models.IntegerField(db_column='oi_size', choices=OITEM_SIZE, default=1)
    oi_qty = models.IntegerField(db_column='io_qty', default=0)
    oi_price = models.DecimalField(db_column='oi_price', max_digits=10, decimal_places=2, null=True, blank=True)
    oi_date = models.DateTimeField(db_column='order_date', blank=True, null=True, auto_now_add=True)
    oi_status = models.IntegerField(db_column='oi_status', choices=Odr.DEL_STATUS, default=1)

    def __str__(self):
        return str(self.oi_type)

    def save(self, *args, **kwargs):
        #store prod_price on a variable
        # if self.oi_type:
        #     poduct_price = self.oi_type.prod_price
        # 
        #     self.oi_price = product_price * self.oi_qty

        # Check if both product and quantity are set
        if self.oi_type and self.oi_qty:
            self.oi_price = self.oi_type.prod_price * self.oi_qty
            

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'tbl_orderItems'
        verbose_name_plural = 'Items'
        verbose_name = 'Item'



