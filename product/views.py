from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView 
from rest_framework import generics
from user.models import ProfileUser

from category.models import Brand, Category
from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
    

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


def ProductsListViews(request):
    brands = Brand.objects.all()
    categores = Category.objects.all()
    template_name = 'shop/index.html'
    products = Product.objects.all()
    context = {
        'products': products,
        'brands': brands,
        'categores': categores
    }
    return render(request, template_name, context=context)


def ProductDetailViews(request, pk):
    product = get_object_or_404(Product, pk=pk)
    porducts_related_store = Product.objects.filter(vendor=product.vendor.id)
    
    vendor = ProfileUser.objects.filter(vendor = product.vendor)
    print('-----------------------------')
    print(vendor)
    template_name = 'shop/product_detail.html'
    context = {
        'product': product,
        'porducts_related_store':porducts_related_store,
        'vendor':vendor
    }
    return render(request, template_name, context=context)
