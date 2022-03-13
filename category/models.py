from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='', unique=True)
    category_logo = models.CharField( max_length=255, default='tshirt2')
    owner = models.ForeignKey('auth.User', related_name='categories',
                              on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class SubCategories(models.Model):
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='sub_categories')
    title=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    thumbnail=CloudinaryField('media/uploads/subcategories')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
class Brand(models.Model):
    logo = CloudinaryField('media/uploads/brands')
    name = models.CharField(max_length=255)
    tag_brand = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class TagProduct(models.Model):
    tage_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tage_name 


class RecommendProduct(models.Model):
    tage_name = models.CharField(max_length=255,default='non')
    
    def __str__(self):
        return self.tage_name
