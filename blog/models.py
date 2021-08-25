from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    thumbnail= models.ImageField(upload_to ='blog/photo/')
    description = models.TextField()
    short_description =models.TextField()
    creation = models.DateTimeField(auto_now_add=True)


    def __str__(self):
         return self .title

    def __str__(self):
         return self .name