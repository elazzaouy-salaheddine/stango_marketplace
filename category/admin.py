from django.contrib import admin
from .models import Category, Brand, TagProduct,RecommendProduct
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(TagProduct)
admin.site.register(RecommendProduct)