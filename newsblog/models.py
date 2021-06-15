from django.db import models

# Create your models here.
class Post(models.Model):
  STATUS = (
    (0,"Draft"),
    (1,"Publish")
  )

  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)
  publish_on = models.DateTimeField(null=True, blank=True)
  
  def __str__(self):
    return self.title

class Comment(models.Model):
  comment = models.TextField()
  author = models.CharField(max_length=100, blank=True, null=True)
  created_on = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Category (models.Model):
  name = models.CharField(max_length=100,blank=True, null=True)
  post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Author (models.Model):
  name = models.CharField(max_length=100,blank=True, null=True)
  post = models.ForeignKey('Post', on_delete=models.CASCADE)

class About (models.Model):
  title = models.CharField(max_length=200, unique=True)
  body = models.TextField()

 
