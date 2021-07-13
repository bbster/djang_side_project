from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    fields = ['content', 'user', 'board']
    list_display = ('id', 'content', 'user', 'board', 'created_at', 'updated_at')


admin.site.register(Comment, CommentAdmin)
