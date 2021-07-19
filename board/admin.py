from django.contrib import admin
from .models import Board, Post, Comment


class BoardAdmin(admin.ModelAdmin):
    fields = ['type']
    list_display = ('id', 'type')


class PostAdmin(admin.ModelAdmin):
    fields = ['board_type', 'title', 'content', 'creator']
    list_display = ('id', 'board_type', 'title', 'content', 'creator', 'created_at', 'updated_at')


class CommentAdmin(admin.ModelAdmin):
    fields = ['post', 'content', 'parent', 'creator']
    list_display = ('id', 'post', 'content', 'parent', 'creator', 'created_at', 'updated_at')


admin.site.register(Board, BoardAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
