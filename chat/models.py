from django.contrib.auth.models import User
from user.models import ProfileUser
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user_01 = models.ForeignKey(
        ProfileUser, related_name='user_01', on_delete=models.CASCADE)
    user_02 = models.ForeignKey(
        ProfileUser, related_name='user_02', on_delete=models.CASCADE)


class Message(models.Model):
    room = models.ForeignKey(
        Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
