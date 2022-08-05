from ast import Or
from pyclbr import Class
from django.dispatch import receiver
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
from .models import ProfileUser, Relationship
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics
from .froms import ProductForm, ProductImagesForm, ProfileForm, RegisterForm, ProductImagesFormSet, OrderForm, OrderShipperForm
from user import serializers
from app import settings
from .serializers import ProfileSerializer
from django.views.generic import ListView
from user.models import ProfileUser
from comment.models import Comment
from order.models import Order, ShippingAddress, OrderShipper
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from comment.models import Comment
from django.contrib import messages
from django.db.models import Q


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


def ShipperProfileView(request, pk):
    shipper = get_object_or_404(ProfileUser, pk=pk)
    context = {
        'shipper': shipper
    }
    template_name = 'user/shipper_profile_detail.html'
    return render(request, template_name, context)


def BecomeVendor(request):
    context = {}
    template_name = 'user/BecomeVendor.html'
    return render(request, template_name, context)


def ProfileViews(request):
    profile = ProfileUser.objects.get(vendor=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'user/profile.html', context)


def invites_received_view(request):
    profile = ProfileUser.objects.get(vendor=request.user)
    qs = Relationship.objects.invatations_received(profile)

    context = {
        'qs': qs
    }
    return render(request, 'user/my_invites.html', context)


class mysippersProfileListView(ListView):
    model = ProfileUser
    template_name = 'user/myshipperlistview.html'
    # context_object_name = 'qs'

    def get_queryset(self):
        qs = ProfileUser.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            user = User.objects.get(
                username__iexact=self.request.user.username)
            profile = ProfileUser.objects.get(vendor=user)
            rel_r = Relationship.objects.filter(sender=profile)
            rel_s = Relationship.objects.filter(receiver=profile)
            rel_receiver = []
            rel_sender = []
            for item in rel_r:
                rel_receiver.append(item.receiver.vendor)
            for item in rel_s:
                rel_sender.append(item.sender.vendor)

            context["rel_receiver"] = rel_receiver
            context["rel_sender"] = rel_sender
            context['is_empty'] = False
            if len(self.get_queryset()) == 0:
                context['is_empty'] = True

            return context


class sippersProfileListView(ListView):
    model = ProfileUser
    template_name = 'user/profile_list.html'
    #context_object_name = 'qs'

    def get_queryset(self):

        qs = ProfileUser.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            user = User.objects.get(
                username__iexact=self.request.user.username)
            profile = ProfileUser.objects.get(vendor=user)
            rel_r = Relationship.objects.filter(sender=profile)
            rel_s = Relationship.objects.filter(receiver=profile)
            rel_receiver = []
            rel_sender = []
            for item in rel_r:
                rel_receiver.append(item.receiver.vendor)
            for item in rel_s:
                rel_sender.append(item.sender.vendor)

            context["rel_receiver"] = rel_receiver
            context["rel_sender"] = rel_sender
            context['is_empty'] = False
            if len(self.get_queryset()) == 0:
                context['is_empty'] = True

            return context


def send_invitations(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = ProfileUser.objects.get(vendor=user)
        receiver = ProfileUser.objects.get(pk=pk)
        rel = Relationship.objects.create(
            sender=sender, receiver=receiver, status='send')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profilesListViews')


def accept_invatation(request):
    if request.method == "POST":
        pk = request.POST.get('profile_pk')
        sender = ProfileUser.objects.get(pk=pk)
        receiver = ProfileUser.objects.get(vendor=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()
    return redirect('profilesListViews')


def reject_invatation(request):
    if request.method == "POST":
        pk = request.POST.get('profile_pk')
        receiver = ProfileUser.objects.get(vendor=request.user)
        sender = ProfileUser.objects.get(pk=pk)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        rel.delete()
    return redirect('profilesListViews')


def remove_from_friends(request):
    if request.method == 'POST':
        pk = request.POST.get('profile_pk')
        user = request.user
        sender = ProfileUser.objects.get(vendor=user)
        receiver = ProfileUser.objects.get(pk=pk)

        rel = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (
                Q(sender=receiver) & Q(receiver=sender))
        )
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profilesListViews')


def invite_profiles_list_view(request):
    user = request.user
    qs = ProfileUser.objects.get_all_profiles_to_invite(user)

    context = {'qs': qs}

    return render(request, 'user/to_invite_list.html', context)


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
        return redirect("store_products")

    return render(request, "user/account_layout/product-delete.html", context)


def StoreOrders(request):
    orderItems = OrderItem.objects.filter(
        product__vendor=request.user).order_by('-date_add')
    orders = []
    for orderItem in orderItems:
        orders.append(orderItem.order)
    order = list(dict.fromkeys(orders))
    total_orders_value = 0
    total_orders_paid = 0
    total_orders_unpaid = 0
    total_orders_return = 0
    for item in order:
        total_orders_value += item.get_cart_total
        if item.Payment_status == 'Paid':
            total_orders_paid += item.get_cart_total
        if item.Payment_status == 'Unpaid':
            total_orders_unpaid += item.get_cart_total
        if item.Shipping_status == 'Return':
            total_orders_return += item.get_cart_total
    template_name = 'user/account_layout/orders_list.html'

    context = {
        'orders': order,
        'orderItems': orderItems,
        'total_orders_value': total_orders_value,
        'total_orders_paid': total_orders_paid,
        'total_orders_unpaid': total_orders_unpaid,
        'total_orders_return': total_orders_return
    }
    return render(request, template_name, context)


def PaidOrders(request):
    orderItems = OrderItem.objects.filter(
        product__vendor=request.user).order_by('-date_add')
    orders = []
    for orderItem in orderItems:
        orders.append(orderItem.order)
    order = list(dict.fromkeys(orders))
    paid_orders = []
    for item in order:
        if item.Payment_status == 'Paid':
            paid_orders.append(item)
    template_name = 'user/account_layout/paid_order.html'
    context = {
        'orders': paid_orders,
        'orderItems': orderItems}
    return render(request, template_name, context)


def ShippedOrders(request):
    orderItems = OrderItem.objects.filter(
        product__vendor=request.user).order_by('-date_add')
    orders = []
    for orderItem in orderItems:
        orders.append(orderItem.order)
    order = list(dict.fromkeys(orders))
    shipped_orders = []
    for item in order:
        if item.Shipping_status == 'Shipped':
            shipped_orders.append(item)
    template_name = 'user/account_layout/shipped_orders.html'
    context = {
        'orders': shipped_orders,
        'orderItems': orderItems}
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


def OrderUpdate(request, pk):
    obj = get_object_or_404(Order, id=pk)
    profile = ProfileUser.objects.get(vendor=request.user)
    orderForm = OrderForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if orderForm.is_valid():
            orderForm.save()
            return redirect("store_orders")
    context = {
        'orderForm': orderForm,
        'obj': obj,
        'profile': profile
    }
    return render(request, "user/account_layout/order-update.html", context)


def OrderUpdateShipper(request, pk):
    ordershipper = get_object_or_404(OrderShipper, id=pk)
    profile = ProfileUser.objects.get(vendor=request.user)
    shipperslist = profile.shippers.all()
    if request.method == 'POST':
        OrderShipperFormvies = OrderShipperForm(
            request.POST or None, instance=ordershipper)
        if OrderShipperFormvies.is_valid():
            OrderShipperFormvies.save()
            return redirect("store_orders")
    else:
        OrderShipperFormvies = OrderShipperForm(
            instance=ordershipper, shippers=shipperslist)
    context = {
        'OrderShipperFormvies': OrderShipperFormvies,
        'profile': profile,
        'shipperslist': shipperslist
    }
    return render(request, "user/account_layout/order-update-shipper.html", context)
