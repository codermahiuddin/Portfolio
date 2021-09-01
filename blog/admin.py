from django.contrib import admin
from .models import Post, Comment

# Register your models here


class PostAdmin(admin.ModelAdmin):
    list_display=[ 
        'title',
        'thumbnail',
        'description'
    ]

admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'body'
      
    ]

admin.site.register(Comment, CommentAdmin)

