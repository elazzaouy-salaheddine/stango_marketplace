from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProfileUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'products',
                  'comments', 'categories']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ['store_name','email','phone_number','city','sotre_banner','sotre_logo']