from django.contrib import admin
from .models import Auth


class AuthAdmin(admin.ModelAdmin):
    fields = ['email', 'username', 'password']
    list_display = ('id', 'email', 'username', 'password')


admin.site.register(Auth, AuthAdmin)
