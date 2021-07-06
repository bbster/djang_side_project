from django.contrib import admin
from .models import Boards


class BoardsAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'user']
    list_display = ('id', 'title', 'text', 'user')


admin.site.register(Boards, BoardsAdmin)
