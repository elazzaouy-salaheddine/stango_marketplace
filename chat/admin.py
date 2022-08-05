from django.contrib import admin

from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_01', 'user_02')


admin.site.register(Room, RoomAdmin)
