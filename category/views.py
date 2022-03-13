from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from product.models import Product
from product.permissions import IsOwnerOrReadOnly
from .models import Brand, Category, SubCategories
from .serializers import CategorySerializer, BrandSerializer
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class BarndList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def index(request):
    sub_categories = SubCategories.objects.all()
    context_dict = {
        'categories': Category.objects.all(),
        'sub_categories': sub_categories
    }

    # Render the response and send it back!
    return render(request, 'categories/index.html', context_dict)


def category_details(request, slug):
    context_dict = {}
    popular_brand = Brand.objects.filter(tag_brand='PopularBrand')[:7]

    try:
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.get(slug=slug)
        context_dict['category_name'] = category.name
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass
    pagi = Paginator(products, 30)
    page = request.GET.get('page')
    products = pagi.get_page(page)
    context_dict['popular_brand'] = popular_brand
    context_dict['products'] = products
    # Go render the response and return it to the client.
    return render(request, 'categories/category.html', context_dict)
