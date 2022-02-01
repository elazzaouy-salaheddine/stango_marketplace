from django.db import models
from ckeditor.fields import RichTextField
from category.models import Category, TagProduct


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.ManyToManyField(Category, 
                                      related_name='product_category')
    photo = models.ImageField(upload_to='media/uploads/products/')
    product_short_desc = models.TextField()
    price = models.FloatField()
    description = RichTextField(blank=True, default='')
    color = models.CharField(null=True, blank=True, max_length=255)
    size = models.CharField(null=True, blank=True, max_length=255)
    detail = models.TextField()
    vendor = models.ForeignKey('auth.User',
                               related_name='vendor',
                               on_delete=models.CASCADE)
    tag = models.ManyToManyField(TagProduct, 
                                      related_name='product_tag')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
