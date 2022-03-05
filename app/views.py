from django.shortcuts import render
from order.models import *
from order.models import Order
from order.utils import cartData
from django.http import JsonResponse

# Create your views here.


def CartTemplate(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items'] 
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems
    }
    template_name = 'base/cart.html'
    return render(request, template_name, context)

