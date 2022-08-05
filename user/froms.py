from pyexpat import model
from urllib import request
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, EmailField, PasswordInput, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from order.models import Order, OrderShipper
from .models import ProfileUser
from product.models import Product, ProductImages
from category.models import Category, SubCategories
from django import forms
from django.forms import ModelChoiceField


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        exclude = ['vendor', 'product', 'shippers']

    def clean(self):
        data = self.cleaned_data
        store_name = data.get("store_name")
        qs = ProfileUser.objects.filter(store_name__iexact=store_name).exclude(
            store_name__iexact=store_name)
        if qs.exists():
            forms.ValidationError(
                "store_name", f"\"{store_name}\" is already in use. Please pick another store name.")
        return data


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['custemer']


class OrderShipperForm(forms.ModelForm):
    user_choice = ModelChoiceField(
        widget=forms.RadioSelect,
        queryset=None,
        empty_label=None,
        label='Please select'
    )

    def __init__(self, shippers, *args, **kwargs):
        super(OrderShipperForm, self).__init__(*args, **kwargs)
        self.fields['user_choice'].queryset = ProfileUser.objects.all().filter(
            shippers=ProfileUser.shippers)

    class Meta:
        model = OrderShipper
        fields = ['order_shipper']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['vendor', 'recommend_product']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_category'].queryset = SubCategories.objects.none()
        if 'category' in self.data:
            try:
                category = int(self.data.get('category'))
                self.fields['sub_category'].queryset = SubCategories.objects.filter(
                    category_id=category).order_by('title')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['category'].queryset = Category.objects.all()
            self.fields['sub_category'].queryset = SubCategories.objects.all()


class ProductImagesForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        exclude = ['product_image']


ProductImagesFormSet = inlineformset_factory(Product, ProductImages,
                                             form=ProductImagesForm, extra=3)
