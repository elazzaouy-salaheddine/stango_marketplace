from order.models import Order, OrderItem
from order.utils import cookieCart

def categories(request):
    from category.models import Category
    return {'categories': Category.objects.all()}

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