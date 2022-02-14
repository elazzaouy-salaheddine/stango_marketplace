from operator import truediv
from django.db import models
from product.models import Product
from ckeditor.fields import RichTextField
# Create your models here.
import uuid
from PIL import Image

class ProfileUser(models.Model):
    store_name = models.CharField(max_length=100, blank=True,null=False, unique=True, default=uuid.uuid1, error_messages ={
                    "unique":"The store must be unique "
                    })
    sotre_banner = models.ImageField(upload_to='media/uploads/vendors',default='default/1.jpg')
    sotre_logo = models.ImageField(upload_to='media/uploads/vendors', default='default/1.jpg')
    email = models.EmailField(null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    description = RichTextField(blank=True, default='')
    vendor = models.OneToOneField('auth.User', related_name='vendor_profile',
                            on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,
                            related_name='vendor_products')
    Shipping_Policy = RichTextField(blank=True, default='')
    Refund_Policy = RichTextField(blank=True, default='')
    Return_Policy = RichTextField(blank=True, default='')
    
    
    class Meta:
        verbose_name_plural = 'vendor_profile'

    def save(self, *args, **kwargs):
        super().save()
        self.sotre_banner = Image.open(self.sotre_banner.path)
        self.sotre_logo = Image.open(self.sotre_logo.path)

    
    def __str__(self):
        return self.store_name
