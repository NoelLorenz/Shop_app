from django.db import models
import uuid


# Create your models here.
class Address(models.Model):
    BARANGAY = [
        (1, 'Andagao'),
        (2, 'Bachaw Norte'),
        (3, 'Bachaw Sur'),
        (4, 'Briones'),
        (5, 'Buswang New '),
        (6, 'Buswang Old '),
        (7, 'Caano'),
        (8, 'Estancia'),
        (9, 'Linabuan Norte'),
        (10, 'Mabilo'),
        (11, 'Mobo'),
        (12, 'Nalook'),
        (13, 'Poblacion'),
        (14, 'Pook'),
        (15, 'Tigayon'),
        (16, 'Tinigaw'),
    ]

    adr_id = models.UUIDField(db_column='adr_id', primary_key=True, default=uuid.uuid4, editable=False)
    adr_barangay = models.CharField(db_column='adr_barangay', max_length=255, blank=False, null=False)
    # adr_municipality

    def __str__(self):
        return self.adr_barangay

    class Meta:
        db_table = 'tbl_address'
        verbose_name_plural = 'Addresses'
        verbose_name = 'Address'



class Customers(models.Model):
    cus_id = models.UUIDField(db_column='cus_id', primary_key=True, default=uuid.uuid4, editable=False)
    cus_name = models.CharField(db_column='cus_name', max_length=255, blank=False, null=False)
    cus_contact = models.CharField(db_column='cus_contact', max_length=255, blank=False, null=False)
    # buyer_address_id = models.ForeignKey(Address, db_column='buyer_address_id', on_delete=models.CASCADE,  null=True, blank=True)
    cus_address_id = models.IntegerField(db_column='cus_address_id', choices=Address.BARANGAY, default=1)

    def __str__(self):
        return self.cus_name

    class Meta:
        db_table = 'tbl_Customers'
        verbose_name_plural = 'Customers'
        verbose_name = 'Customer'

class Products(models.Model):
    prod_id = models.UUIDField(db_column='cus_id', primary_key=True, default=uuid.uuid4, editable=False)
    prod_name = models.CharField(db_column='cus_name', max_length=255, blank=False, null=False)
    prod_price = models.DecimalField(db_column='oi_price', max_digits=10, decimal_places=2, blank=False, null=False,
                                     default=0.00)

    def __str__(self):
        return self.prod_name

    class Meta:
        db_table = 'tbl_Products'
        verbose_name_plural = 'Products'
        verbose_name = 'Product'