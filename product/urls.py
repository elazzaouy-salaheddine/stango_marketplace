from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductDetail, ProductList, ProductsListViews, ProductDetailViews, ProductSearch
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/', ProductList.as_view()),
    path('api/<int:pk>/', ProductDetail.as_view()),
    path('', ProductsListViews, name='shop'),
    path('<int:pk>/', ProductDetailViews, name='product_details'),
    path('serach-products/', ProductSearch, name='serach_products'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
