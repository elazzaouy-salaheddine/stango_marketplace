from tokenize import blank_re
from django.db import models
from product.models import Product
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
# Create your models here.
import uuid
from PIL import Image

class ProfileUser(models.Model):
    store_name = models.CharField(max_length=100, blank=True,null=False, unique=True, default=uuid.uuid1, error_messages ={
                    "unique":"The store must be unique "
                    })
    sotre_banner = CloudinaryField('media/uploads/vendors',default='v1645988134/default/1_yf3l0n.jpg')
    sotre_logo = CloudinaryField('media/uploads/vendors', default='v1645988456/default/1.jpg')
    email = models.EmailField(null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    vendor = models.OneToOneField('auth.User', related_name='vendor_profile',
                            on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,
                            related_name='vendor_products')
    Shipping_Policy = RichTextField(null=True, blank=True)
    Refund_Policy = RichTextField(null=True, blank=True)
    Return_Policy = RichTextField(null=True, blank=True)
    facebook_link = models.URLField(max_length=255, null=True, blank=True)
    twitter_link = models.URLField(max_length=255, null=True, blank=True)
    instagram_link = models.URLField(max_length=255, null=True, blank=True)
    watsapp_link = models.IntegerField(null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = 'vendor_profile'
    
    def __str__(self):
        return self.store_name
