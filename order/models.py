from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
from product.models import Product
# Create your models here.
from django.db.models.signals import post_save

from user.models import ProfileUser


class Custemer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True, related_name='custemer')
    name = models.CharField(max_length=25, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        if self.name == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.name


class Order(models.Model):
    Delivered = 'Delivered'
    Return = 'Return'
    Unknown = 'Unknown'
    Shipped = 'Shipped'
    SHIPPING_CHOICES = [
        (Shipped, 'Shipped'),
        (Delivered, 'Delivered'),
        (Return, 'Return'),
        (Unknown, 'Unknown'),
    ]
    Unpaid = 'Unpaid'
    Paid = 'Paid'
    PAYMENT_CHOICES = [
        (Unpaid, 'Unpaid'),
        (Paid, 'Paid'),
    ]
    No_Reply = 'No Reply'
    Confirmed = 'Confirmed'
    Canceled = 'Canceled'
    Call_Center_CHOICES = [
        (No_Reply, 'No Reply'),
        (Confirmed, 'Confirmed'),
        (Canceled, 'Canceled'),
        (Unknown, 'Unknown'),
    ]
    custemer = models.ForeignKey(
        Custemer, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    Payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICES,
        default=Unpaid,
    )
    Shipping_status = models.CharField(
        max_length=10,
        choices=SHIPPING_CHOICES,
        default=Unknown,
    )
    Call_Center_status = models.CharField(
        max_length=10,
        choices=Call_Center_CHOICES,
        default=Unknown,
    )
    myshipper = models.ManyToManyField(
        ProfileUser, blank=True, related_name='myshipperuser')

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        cart_total = sum([item.get_total for item in orderitems])
        return cart_total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        cart_total_items = sum([item.quantity for item in orderitems])
        return cart_total_items


class OrderItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_add',)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    custemer = models.ForeignKey(
        Custemer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
