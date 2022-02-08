from django.urls import path
from .views import cart, checkout, updateItem, orderComplet

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('updateitem/', updateItem, name='updateitem'),
    path('order-complet/', orderComplet, name='ordercomplet'),
]
