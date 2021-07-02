from django.contrib import admin
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    fields = ['email', 'username', 'password']
    list_display = ('id', 'email', 'username', 'password')


admin.site.register(Users, UsersAdmin)
