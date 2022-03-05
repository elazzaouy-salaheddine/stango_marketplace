import json
from .models import *
from product.models import Product


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
            'shipping': False
            }
    cartItems = order['get_cart_items']
    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
        
            item = {
                    'product': {
                        'id': product.id,
                        'title': product.title,
                        'price': product.price,
                        'photo': product.photo,
                        },
                    'quantity': cart[i]['quantity'],
                    'get_total': total
                    }
            items.append(item)
            if product.digital is False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    if request.user.is_authenticated:
        custemer = request.user.custemer
        order, created = Order.objects.get_or_create(custemer=custemer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    name = data['form']['name']
    phone_number = data['form']['phone_number']
    cookkieData = cookieCart(request)
    items = cookkieData['items']
        
    custemer, created = Custemer.objects.get_or_create(
        phone_number=phone_number
    )
    custemer.name = name
    custemer.save()
    order = Order.objects.create(
        custemer=custemer,
        complete = False,
    )
    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            order = order,
            product=product,
            quantity =item['quantity'],
        )
    return custemer, order