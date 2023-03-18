from django.db import models

class BlogPost(models.Model):
    title = models.TextField(default="Enter title here")
    slug = models.SlugField(unique=True, default="Enter Slug here")
    content = models.TextField(null=True, blank=True, default="Enter content here")                                                                                                                               
