from django.db import models
from ckeditor.fields import RichTextField
from category.models import Category, TagProduct, RecommendProduct
from PIL import Image

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    category = models.ManyToManyField(Category, 
                                      related_name='product_category')
    recommend_product = models.ManyToManyField(RecommendProduct, default='non',
                                      related_name='product_recommend')
    photo = models.ImageField(upload_to='media/uploads/products/', help_text='image size nice to be 300*338')
    product_short_desc = models.TextField()
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
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
    
    def save(self):
        super().save()
        self.photo = Image.open(self.photo.path)

    def __str__(self):
        return self.title
