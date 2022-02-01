from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductDetail, ProductList, ProductsListViews, ProductDetailViews


urlpatterns = [
    path('api/', ProductList.as_view()),
    path('api/<int:pk>/', ProductDetail.as_view()),
    path('', ProductsListViews, name='shop'),
    path('<int:pk>/', ProductDetailViews, name='product_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
