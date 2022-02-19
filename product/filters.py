from .models import Product
import django_filters


class ProductFilter(django_filters.FilterSet):
    #title = django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    #category = django_filters.MultipleChoiceFilter(field_name='category')
    class Meta:
        model = Product
        fields = ['category']
