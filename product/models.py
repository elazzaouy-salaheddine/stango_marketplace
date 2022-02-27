from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField
from category.models import Category, TagProduct, RecommendProduct, SubCategories
from cloudinary.models import CloudinaryField
from PIL import Image

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.ForeignKey(Category, related_name='product_category_parent', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategories, related_name='product_sub_category', on_delete=models.CASCADE)
    recommend_product = models.ManyToManyField(RecommendProduct, default='non',
                                      related_name='product_recommend')
    photo = CloudinaryField('media/uploads/products/', help_text='image size nice to be 300*338')
    product_short_desc = models.TextField(max_length=500)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    color = models.CharField(null=True, blank=True, max_length=255)
    size = models.CharField(null=True, blank=True, max_length=255)
    detail = models.TextField()
    vendor = models.ForeignKey('auth.User',
                               related_name='vendor',
                               on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
