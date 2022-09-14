from django.contrib import admin

# Register your models here.
from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list = ('title', 'content', 'author', 'date_posted')

admin.site.register(Posts, PostsAdmin)
