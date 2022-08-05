from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message
from user.models import ProfileUser


@login_required
def index(request):
    rooms = Room.objects.all()
    profile = ProfileUser.objects.get(vendor=request.user)

    return render(request, 'chat/index.html', {'rooms': rooms, 'profile': profile})


@login_required
def room(request, slug):
    rooms = Room.objects.all()
    profile = ProfileUser.objects.get(vendor=request.user)
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room.html', {'rooms': rooms, 'profile': profile, 'room': room, 'messages': messages})
