from re import I
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ProfileUser, Relationship
from chat.models import Room
from order.models import Custemer, OrderShipper, Order


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(vendor=instance)
        Custemer.objects.create(user=instance)


@receiver(post_save, sender=Order)
def save_profile(sender, created, instance, **kwargs):
    if created:
        OrderShipper.objects.create(order=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.vendor


@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):

    sender_ = instance.sender
    receiver_ = instance.receiver
    roome_name = str(instance.sender) + str(instance.receiver)
    room_slug = roome_name

    if instance.status == 'accepted':
        sender_.shippers.add(receiver_.vendor)
        receiver_.shippers.add(sender_.vendor)
        sender_.save()
        receiver_.save()
        Room.objects.create(name=roome_name, slug=room_slug,
                            user_01=sender_, user_02=receiver_)


@receiver(pre_delete, sender=Relationship)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    sender.shippers.remove(receiver.vendor)
    receiver.shippers.remove(sender.vendor)
    sender.save()
    receiver.save()
