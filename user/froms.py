from pyexpat import model
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, EmailField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import ProfileUser
from product.models import Product

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit :
            user.save()
        return user
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        exclude = ['vendor','product']
    
    def clean(self):
        data = self.cleaned_data
        store_name = data.get("store_name")
        qs = ProfileUser.objects.filter(store_name__iexact=store_name).exclude(store_name__iexact=store_name)
        if qs.exists():
            forms.ValidationError("store_name", f"\"{store_name}\" is already in use. Please pick another store name.")
        return data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['vendor','recommend_product']

        