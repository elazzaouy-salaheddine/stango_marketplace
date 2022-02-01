from django.contrib import admin
from .models import ProfileUser
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('store_name','email','phone_number','city')
    
    
admin.site.register(ProfileUser,ProfileAdmin)