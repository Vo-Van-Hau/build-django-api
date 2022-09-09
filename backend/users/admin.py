from django.contrib import admin

# Register your models here.
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list = ('username', 'email', 'name', 'password')

admin.site.register(Users, UsersAdmin)