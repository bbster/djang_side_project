from django.contrib import admin
from .models import Boards, Comment


class BoardAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'creator']
    list_display = ('id', 'title', 'content', 'creator', 'created_at', 'updated_at')


class CommentAdmin(admin.ModelAdmin):
    fields = ['board', 'content', 'creator']
    list_display = ('id', 'board', 'content', 'creator', 'created_at', 'updated_at')


admin.site.register(Boards, BoardAdmin)
admin.site.register(Comment, CommentAdmin)
