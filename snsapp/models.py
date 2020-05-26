from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PostModel(models.Model):
    user_id = models.IntegerField()
    content = models.TextField(max_length = 140)
    images = models.ImageField(upload_to="post")

class GoodModel(models.Model):
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    count_id = models.IntegerField()

class FollowModel(models.Model):
    user_id = models.IntegerField()
    follow_id = models.IntegerField()

class FollowerwModel(models.Model):
    user_id = models.IntegerField()
    follower_id = models.IntegerField()

class IntoroductionModel(models.Model):
    user_id = models.IntegerField()
    introduction = models.TextField(max_length = 140)
    url = models.URLField(max_length=200)
