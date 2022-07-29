from tokenize import blank_re
from django.db import models
from product.models import Product
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
# Create your models here.
import uuid
from PIL import Image
from django.db.models import Q


class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self, sender):
        profiles = ProfileUser.objects.all().exclude(vendor=sender)
        profile = ProfileUser.objects.get(vendor=sender)
        qs = Relationship.objects.filter(
            Q(sender=profile) | Q(receiver=profile))

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)

        available = [
            profile for profile in profiles if profile not in accepted]
        return available

    def get_all_profiles(self, me):
        profiles = ProfileUser.objects.all().exclude(vendor=me)
        return profiles


class ProfileUser(models.Model):
    JOB_CHOICES = (
        ('vendor', 'vendror'),
        ('shipper', 'shipper')
    )
    job = models.CharField(max_length=255, choices=JOB_CHOICES)
    store_name = models.CharField(max_length=100, blank=True, null=False, unique=True, default=uuid.uuid1, error_messages={
        "unique": "The store must be unique "
    })
    sotre_banner = CloudinaryField(
        'media/uploads/vendors', default='v1645988134/default/1_yf3l0n.jpg')
    sotre_logo = CloudinaryField(
        'media/uploads/vendors', default='v1645988456/default/1.jpg')
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
    shippers = models.ManyToManyField(
        'auth.User', blank=True, related_name='shippers')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = ProfileManager()

    class Meta:
        verbose_name_plural = 'vendor_profile'

    def get_shippers(self):
        return self.shippers.all()

    def get_shippers_no(self):
        return self.shippers.all().count()

    def __str__(self):
        return self.store_name


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)


class RelationshipManager(models.Manager):
    def invatations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs


class Relationship(models.Model):
    sender = models.ForeignKey(
        ProfileUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        ProfileUser, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
