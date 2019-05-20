from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Keyword(models.Model):
    name = models.CharField(max_length=50, unique=True)


class User(AbstractUser):
    credit = models.IntegerField(default=100)
    influ = models.FloatField(default=0.0)
    is_reviewer = models.BooleanField(default=False)

    keywords = models.ManyToManyField(Keyword, through='UserKeyword')


class UserKeyword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    is_review = models.BooleanField(default=False)


class Article(models.Model):
    title = models.CharField(max_length=255)
    reads = models.IntegerField(default=0)
    pubtime = models.DateField(auto_now_add=True)

    authors = models.ManyToManyField(User)
    keywords = models.ManyToManyField(Keyword)


class Content(models.Model):
    content = models.TextField()
    modif = models.TextField(blank=True)
    sbmt_time = models.DateField(auto_now_add=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    pubtime = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
