from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Product
from django import forms
from ckeditor.widgets import CKEditorWidget
from comment.models import Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor')
    inlines = [CommentInline]
    form = ProductAdminForm



admin.site.register(Product, ProductAdmin)
