from django.forms import formset_factory
from distutils.log import error
from unicodedata import category
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.forms import inlineformset_factory, modelformset_factory
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
from django.contrib import messages
from category.models import Category, SubCategories
from order.models import OrderItem
from product.models import Product, ProductImages
from .models import ProfileUser
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics
from .froms import ProductForm, ProductImagesForm, ProfileForm, RegisterForm, ProductImagesFormSet
from user import serializers
from app import settings
from .serializers import ProfileSerializer
from django.views.generic import ListView
from user.models import ProfileUser
from comment.models import Comment
from order.models import Order, ShippingAddress
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib import messages
from comment.models import Comment
from django.contrib import messages


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ProfileView(generics.ListAPIView):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileSerializer


def RegisterUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        vendor_form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            # store = vendor_form.save(commit=False)
            # store.vendor = user
            # store.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("account_setting")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    vendor_form = ProfileForm()
    return render(request, 'registratio/register.html', context={"register_form": form, "vendor_form": vendor_form})


def StoreView(request):
    vendors = ProfileUser.objects.all()
    template_name = 'user/store.html'
    context = {
        'vendors': vendors
    }
    return render(request, template_name, context)


def SotreDetail(request, store_name):
    store = get_object_or_404(ProfileUser, store_name=store_name)
    store_products = Product.objects.filter(vendor=store.vendor, puslish=True)
    context = {
        'store_products': store_products,
        'store': store
    }
    template_name = 'user/store_detail.html'
    return render(request, template_name, context)


def BecomeVendor(request):
    context = {}
    template_name = 'user/BecomeVendor.html'
    return render(request, template_name, context)


def AccountSetting(request):
    p_form = ProfileForm(request.POST or None, request.FILES,
                         instance=request.user.vendor_profile)
    if request.method == 'POST':
        #u_form = UserUpdateForm(request.POST, instance=request.user)
        try:
            if p_form.is_valid():
                # u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                # Redirect back to profile page
                return redirect('account_setting')
        except IntegrityError as e:
            messages.add_message(
                request, messages.INFO, 'store_name is already in use. Please pick another store name.')
    else:
        #u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.vendor_profile)

    context = {
        'ProfileForm': p_form
    }

    return render(request, 'user/settings/profile_settings.html', context)


def StoreProducts(request):
    products = Product.objects.filter(vendor=request.user)
    template_name = 'user/account_layout/products.html'
    context = {
        'products': products
    }
    return render(request, template_name, context)


# AJAX
def load_sub_categoires(request):
    id_category = request.GET.get('id_category')
    sub_categories = SubCategories.objects.filter(
        category_id=id_category).all()
    return render(request, 'user/account_layout/sub_categories_options.html', {'sub_categories': sub_categories})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def StoreProductCreate(request):
    categories = Category.objects.all()
    product_form = ProductForm(request.POST or None, request.FILES)
    #ProductImagesFormSe = ProductImagesFormSet(request.POST, request.FILES)
    if request.method == "POST":
        if product_form.is_valid():
            form = product_form.save(commit=False)
            form.vendor = request.user
            form.save()
            formset = ProductImagesFormSet(
                request.POST, request.FILES, instance=form)
            if formset.is_valid():
                formset.save()
            messages.success(request, 'product add success')
            messages.error(request, error)
            # return redirect("store_products")
        else:
            messages.warning(request, 'products not created!')
    product_form = ProductForm()
    ProductImagesFormSe = ProductImagesFormSet()
    template_name = 'user/account_layout/product-create.html'
    context = {
        'product_form': product_form,
        'categories': categories,
        'ProductImagesFormSet': ProductImagesFormSe
    }
    return render(request, template_name, context)


# importing formset_factory
def StoreProductUpdate(request, pk, *args, **kwargs):
    obj = get_object_or_404(Product, id=pk)
    product_images = ProductImages.objects.filter(product_image=obj.pk)
    # pass the object as instance in form
    product_form = ProductForm(
        request.POST or None, request.FILES, instance=obj)
    ProductImagesFormSe = modelformset_factory(
        ProductImages, form=ProductImagesForm, extra=2)
    qs = obj.productimages_set.all()
    formset = ProductImagesFormSe(
        request.POST or None, request.FILES, queryset=qs)
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
            formset = ProductImagesFormSet(queryset=qs)
            if formset.is_valid():
                formset.save()
            return redirect("store_products")
    else:
        #u_form = UserUpdateForm(instance=request.user)
        product_form = ProductForm(instance=obj)
        formset = ProductImagesFormSe(queryset=qs)
    print('-------------*******************')
    print(qs)
    context = {
        'product_form': product_form,
        'ProductImagesFormSet': formset,
        'obj': obj,
        'qs': qs,
        'product_images': product_images
    }

    return render(request, "user/account_layout/product-update.html", context)


def StoreProductDelete(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect("store_products")

    return render(request, "user/account_layout/product-delete.html", context)


def StoreOrders(request):
    #orders = Order.objects.all().order_by('-date')
    orderItems = OrderItem.objects.filter(
        product__vendor=request.user).order_by('-date_add')
    orders = []
    for orderItem in orderItems:
        orders.append(orderItem.order)
    order = list(dict.fromkeys(orders))

    template_name = 'user/account_layout/orders_list.html'
    context = {
        'orders': order,
        'orderItems': orderItems
    }
    return render(request, template_name, context)


def SotreOrdersDetail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    orderItems = OrderItem.objects.filter(
        product__vendor=request.user, order=order)
    shippingaddres = ShippingAddress.objects.filter(order=order)
    order_total = 0
    for item in orderItems:
        order_total += item.get_total
    context = {
        'order': order,
        'orderItems': orderItems,
        'order_total': order_total,
        'shippingaddres': shippingaddres
    }
    template_name = 'user/account_layout/store_order_detail.html'
    return render(request, template_name, context)
