from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    hobbe = models.CharField(max_length=255)
    join = models.DateTimeField(auto_now_add=True)


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
