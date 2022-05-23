from django.db import models
from users.models import User


# Create your models here.
class Post(models.Model):
    authorId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=True)
    createAt = models.TimeField(auto_now_add=True, blank=False)
    updateAt = models.TimeField(auto_now_add=True, blank=False)
    content = models.CharField(max_length=1000)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['createAt']


class Comment(models.Model):
    authorId = models.ForeignKey(User, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    createAt = models.TimeField(auto_now_add=True, blank=False)
    content = models.CharField(max_length=500)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['createAt']
