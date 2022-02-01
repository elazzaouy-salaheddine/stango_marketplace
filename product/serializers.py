from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    vendor = serializers.ReadOnlyField(source='vendor.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'photo', 'price',
                  'vendor', 'comments', 'category', 'tag']


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'products', 'comments', 'categories']
