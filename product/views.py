from itertools import product
import json
from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView 
from rest_framework import generics
from user.models import ProfileUser
from .filters import ProductFilter
from category.models import Brand, Category
from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def ProductsSearche(request) :
    if request.method =='POST':
        search_str = json.loads(request.body).get('searche')
        products = Product.objects.filter(title__icontains=search_str)| Product.objects.filter(category__name__icontains=search_str)| Product.objects.filter(tag__tage_name__icontains=search_str)
        data = products.values()
        return JsonResponse(list(data), safe=False)
        
def ProductsListViews(request):
    brands = Brand.objects.all()
    popular_brand = Brand.objects.filter(tag_brand='PopularBrand')
    categores = Category.objects.all()
    template_name = 'shop/index.html'
    products = Product.objects.all()
    my_product_filter = ProductFilter(request.GET, queryset=products)
    products = my_product_filter.qs
    pagi = Paginator(products,30)
    page = request.GET.get('page')
    products = pagi.get_page(page)
    context = {
        'products': products,
        'brands': brands,
        'categores': categores,
        'my_product_filter': my_product_filter,
        'popular_brand':popular_brand    }
    return render(request, template_name, context=context)


def ProductDetailViews(request, pk):
    product = get_object_or_404(Product, pk=pk)
    porducts_related_store = Product.objects.filter(vendor=product.vendor.id)
    
    vendor = ProfileUser.objects.filter(vendor = product.vendor)
    template_name = 'shop/product_detail.html'
    context = {
        'product': product,
        'porducts_related_store':porducts_related_store,
        'vendor':vendor
    }
    return render(request, template_name, context=context)

def ProductSearch(request):
    template_name = 'shop/products_search.html'
    query_dict = request.GET
    query = query_dict.get('title')
    print(query)
    products = Product.objects.filter(title__icontains=query)
    context = {
        'products': products
        }
    return render(request, template_name, context=context)
