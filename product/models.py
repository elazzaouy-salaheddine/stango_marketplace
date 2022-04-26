from statistics import mode
from django.db import models
from ckeditor.fields import RichTextField
from category.models import Category, TagProduct, RecommendProduct, SubCategories
from cloudinary.models import CloudinaryField
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    FRANCHE = 'FR'
    ARABIC = 'AR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRANCHE, 'FRANCHE'),
        (ARABIC, 'ARABIC'),
    ]
    
    created = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRANCHE,
    )
    title = models.CharField(max_length=100, default='')
    category = models.ForeignKey(
        Category, related_name='product_category_parent', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SubCategories, related_name='product_sub_category', on_delete=models.CASCADE)
    recommend_product = models.ManyToManyField(RecommendProduct, default='non',
                                               related_name='product_recommend')
    photo = CloudinaryField('media/uploads/products/',
                            help_text='image size nice to be 300*338')
    product_short_desc = RichTextField(blank=True, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    detail = RichTextUploadingField(blank=True, null=True)
    vendor = models.ForeignKey('auth.User',
                               related_name='vendor',
                               on_delete=models.CASCADE)
    puslish = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product_image = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = CloudinaryField('media/uploads/products/',
                            help_text='image size nice to be 300*338')
