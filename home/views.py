from re import template
from django.shortcuts import render
from product.models import Product
from user.models import ProfileUser
from category.models import Category, Brand
# Create your views here.


def Home(request):
    template_name='home/index.html'
    category_list = Category.objects.all()
    products = Product.objects.all()
    popular_brand = Brand.objects.filter(tag_brand='PopularBrand')
    product_clothing = Product.objects.filter(category__name='Clothing & Apparel')
    product_electric = Product.objects.filter(category__name='Consumer Electric')
    product_garden = Product.objects.filter(category__name='Home Garden & Kitchen')
    deals_hot = Product.objects.filter(recommend_product__tage_name='Top 20')
    product_electric_recommend = Product.objects.filter(recommend_product__tage_name='Recommend',category__name='Consumer Electric')
    product_garden_recommend = Product.objects.filter(recommend_product__tage_name='Recommend',category__name='Home Garden & Kitchen')
    vendors = ProfileUser.objects.all()
    brands = Brand.objects.all()
    context = {
        'products': products,
        'vendors': vendors,
        'brands': brands,
        'popular_brand':popular_brand,
        'product_clothing': product_clothing,
        'product_electric': product_electric,
        'product_garden': product_garden,
        'deals_hot': deals_hot,
        'product_electric_recommend': product_electric_recommend,
        'product_garden_recommend': product_garden_recommend,
        'categories': category_list
        }
    return render(request, template_name, context)


def AboutUs(request):
    template_name= 'home/about_us.html'
    context = {
        
    }
    return render(request, template_name, context)