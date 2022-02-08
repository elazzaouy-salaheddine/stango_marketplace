from argparse import Action
from asyncio import proactor_events
from itertools import product
import json
from math import prod
from platform import java_ver
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def cart(request):
    if request.user.is_authenticated:
        custemer = request.user.custemer
        order, created = Order.objects.get_or_create(custemer=custemer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_total' : 0,
            'get_cart_items' : 0,
            'shipping':False
            }
    context = {
        'items': items,
        'order': order
    }
    template_name = 'order/cart.html'
    return render(request, template_name, context)


def checkout(request):
    if request.user.is_authenticated:
        custemer = request.user.custemer
        order, created = Order.objects.get_or_create(custemer=custemer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
            'shipping':False
            }
    context = {
        'items': items,
        'order': order
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
    
    if orderItem.quantity<=0:
        orderItem.delete()    
    return JsonResponse('item was added', safe=False)

def orderComplet(request):
    return JsonResponse('payement complte')