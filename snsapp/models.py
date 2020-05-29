from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length = 140)
    images = models.ImageField(upload_to="post")

class GoodModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    count = models.IntegerField()

class FollowModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_id = models.IntegerField()

class IntoroductionModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    introduction = models.TextField(max_length = 140)
    url = models.URLField(max_length=200)
    profile_icon = models.ImageField(upload_to="user", blank=True, null=True)
