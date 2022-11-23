from django.contrib import admin
from .models import Post
from .models import Group
from django.db import models

class PostAdmin(admin.ModelAdmin):
    list_editable = ('group',)
    list_display = ('pk', 'text', 'pub_date', 'author', 'group') 
    search_fields = ('text',) 

    list_filter = ('pub_date',) 
    empty_value_display = '-пусто-' 

admin.site.register(Post, PostAdmin)  

class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    list_filter = ('slug',) 
    empty_value_display = '-пусто-' 

admin.site.register(Group, GroupAdmin)
