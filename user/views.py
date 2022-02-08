from re import template
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
from django.contrib import messages
from product.models import Product
from .models import ProfileUser
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import generics
from .froms import ProfileForm, RegisterForm
from user import serializers 
from app import settings
from .serializers import ProfileSerializer
from django.views.generic import ListView
from user.models import ProfileUser
from comment.models import Comment

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
        if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful." )
                return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request,'registration/register.html', context={"register_form":form})


def StoreView(request):
    vendors = ProfileUser.objects.all()
    template_name = 'user/store.html'
    context = {
        'vendors' : vendors
    }
    return render(request, template_name, context)


def SotreDetail(request, pk):
    store = get_object_or_404(ProfileUser, pk=pk)
    store_products = Product.objects.filter(vendor=store.vendor)
    context = {
        'store_products': store_products,
        'store': store
    }
    template_name = 'user/store_detail.html'
    return render(request, template_name, context)


def BecomeVendor(request):
    context = {}
    template_name= 'user/BecomeVendor.html'
    return render(request, template_name, context)


def  AccountSetting(request):
    if request.method == 'POST':
        #u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.vendor_profile) 
        if p_form.is_valid():
            #u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account_setting') # Redirect back to profile page
    else:
        #u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.vendor_profile)

    context = {
        'ProfileForm': p_form
    }

    return render(request, 'user/myaccount.html', context)


def StoreProducts(request):
    products = Product.objects.filter(vendor = request.user)
    template_name = 'user/account_layout/products.html'
    context = {
        'products': products
    }
    return render(request, template_name, context)