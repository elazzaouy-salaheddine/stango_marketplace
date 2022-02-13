import datetime
import json
from math import prod
from re import template
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .utils import cookieCart, cartData, guestOrder

from django.views.decorators.csrf import csrf_protect
# Create your views here.


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items'] 
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    template_name = 'order/cart.html'
    return render(request, template_name, context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems
    }
    template_name = 'order/checkout.html'
    return render(request, template_name, context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    custemer = request.user.custemer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(custemer=custemer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product )
    
    if action=='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action=='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()    
    return JsonResponse('item was added', safe=False)

@csrf_protect
def orderComplet(request):
    date_order = datetime.datetime.now()
    data =json.loads(request.body)
    if request.user.is_authenticated:
        custemer = request.user.custemer
        order, created = Order.objects.get_or_create(custemer=custemer, complete=False)
        
    else:
        custemer, order = guestOrder(request, data)
    total = float(data['form']['total'])
    order.date = date_order
    if total == float(order.get_cart_total):
            order.complete = True
    order.save()
    if order.shipping == True:
        ShippingAddress.objects.create(
            custemer = custemer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city']
            )
    
    return JsonResponse('order complte', safe=False)


def orderViews(request):
    template_name ='order/order_complet.html'
    context = {
        
    }
    return render(request, template_name, context)