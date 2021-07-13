from django.contrib import admin
from .models import Boards


class BoardsAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'user']
    list_display = ('id', 'title', 'content', 'user', 'created_at', 'updated_at')


admin.site.register(Boards, BoardsAdmin)
