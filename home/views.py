from django.shortcuts import render
from product.models import Product
from user.models import ProfileUser
from category.models import Category, Brand
# Create your views here.


def Home(request):
    template_name='home/index.html'
    products = Product.objects.all()
    vendors = ProfileUser.objects.all()
    brands = Brand.objects.all()
    context = {
        'products': products,
        'vendors':vendors,
        'brands':brands
        }
    return render(request, template_name, context)
