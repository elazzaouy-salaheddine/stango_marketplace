from django.contrib import admin
from .models import Category, Brand, TagProduct,RecommendProduct
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')


admin.site.register(Category)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','tag_brand')
    list_filter = ('tag_brand',)
    
admin.site.register(Brand,BrandAdmin)
admin.site.register(TagProduct)
admin.site.register(RecommendProduct)