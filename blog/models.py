from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blog')
