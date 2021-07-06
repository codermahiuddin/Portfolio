from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import  Blogpost, Comment

# Register your models here.

# PostAdmin
class PostAdmin(SummernoteModelAdmin):
    list_display = [
        'title',
        'image',
    ]
    summernote_fields = ('description',)
    prepopulated_fields = {'slug': ['title', ]}


admin.site.register(Blogpost, PostAdmin)


# CommentAdmin
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'body'
    ]

admin.site.register(Comment, CommentAdmin)