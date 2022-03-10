from pyexpat import model
from django.contrib import admin
from django.forms import inlineformset_factory
from .models import Product, ProductImages
from django import forms
from ckeditor.widgets import CKEditorWidget
from comment.models import Comment
# Register your models here.
from ckeditor_uploader.fields import RichTextUploadingField

class CommentInline(admin.TabularInline):
    model = Comment

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    
    
class ProductAdminForm(forms.ModelForm):
    detail = RichTextUploadingField()
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'vendor')
    inlines = [CommentInline, ProductImagesInline]
    form = ProductAdminForm



admin.site.register(Product, ProductAdmin)
