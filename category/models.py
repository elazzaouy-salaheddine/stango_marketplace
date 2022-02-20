from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    category_logo = models.CharField( max_length=255, default='tshirt2')
    owner = models.ForeignKey('auth.User', related_name='categories',
                              on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


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
