from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

# Blog Post Model
class Blogpost(models.Model):
    title = models.CharField(max_length=250)
    tags = TaggableManager()
    image = models.ImageField(upload_to='post/', blank=True, null=True)
    description = models.TextField(max_length=5000)
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    read = models.IntegerField(default=0)

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
    

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Blogpost, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    email = models.CharField(max_length=150)
    creation = models.DateTimeField(auto_now_add=True)
