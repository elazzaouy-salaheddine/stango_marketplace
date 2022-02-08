from django.contrib import admin
from .models import Order, OrderItem, Custemer, ShippingAddress
# Register your models here.


admin.site.register(Order)
admin.site.register(Custemer)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
