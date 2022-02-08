from django.contrib.auth.models import User
from django.db import models
from product.models import Product
# Create your models here.


class Custemer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True, related_name='custemer')
    name = models.CharField(max_length=25, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    custemer = models.ForeignKey(Custemer, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping=True
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

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    custemer = models.ForeignKey(Custemer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
