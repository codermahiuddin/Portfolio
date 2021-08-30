from django.db import models
from django.urls import reverse
# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=80)
    slug =models.SlugField()
    thumbnail= models.ImageField(upload_to ='blog/photo/')
    description = models.TextField()
    short_description =models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self .title


     

    def get_absolute_url(self):
         return reverse("blog:blog_details", kwargs={
              "slug": self.slug
              })
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()



class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
