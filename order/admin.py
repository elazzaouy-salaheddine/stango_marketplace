from django.contrib import admin
from .models import Order, OrderItem, Custemer, ShippingAddress
# Register your models here.

class CustemerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    
    
admin.site.register(Order)
admin.site.register(Custemer, CustemerAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
