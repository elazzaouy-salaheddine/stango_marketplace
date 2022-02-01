from django.contrib import admin
from.models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'owner')


admin.site.register(Comment, CommentAdmin)
