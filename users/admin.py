from django.contrib import admin
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    fields = ['username', 'password']
    list_display = ('id', 'username', 'password')


admin.site.register(Users, UsersAdmin)
