from re import template
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic import FormView

from product.models import Product
from .models import ProfileUser
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .froms import RegisterForm
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
    return render(request,'registration/register.html')


def register_new_user(form, request):
    existing_user = User.objects.filter(email=form.cleaned_data['email'])

    if existing_user.exists():
        password_reset_url = request.scheme + '://' + request.get_host() + reverse('password_reset')
        existing_user.first().email_user(get_template('emails/already_registered_subject.txt').render(context={'site_name': settings.SITE_NAME}),
                                         get_template('emails/already_registered.html').render(context={'password_reset_url': password_reset_url}))
        raise IntegrityError("Email already exists: %s" % form.cleaned_data['email'])
    else:
        # Create and log in user
        newly_created_user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'])
        login(request, newly_created_user)


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):

        try:
            register_new_user(form, self.request)
            messages.success(self.request, 'Thank you for registering. You have been automatically logged in.')
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        except IntegrityError as e:
            print("Error when registering a new user: %s" % e)
            return HttpResponse(get_template('registration/registration_complete.html').render())


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
    
    #reviews = Comment.objects.filter(product=store_products)
    #print('++++++++++++++++++++++++++++')
    #print(reviews)
    context = {
        'store_products': store_products,
        'store': store,
        #'reviews':reviews
    }
    template_name = 'user/store_detail.html'
    return render(request, template_name, context)


def BecomeVendor(request):
    context = {}
    template_name= 'user/BecomeVendor.html'
    return render(request, template_name, context)
