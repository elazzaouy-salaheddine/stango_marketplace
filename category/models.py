from select import select
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    category_logo = models.ImageField(upload_to='media/uploads/categores')
    owner = models.ForeignKey('auth.User', related_name='categories',
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    logo = models.ImageField(upload_to='media/uploads/brands')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class TagProduct(models.Model):
    tage_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tage_name
