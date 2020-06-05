from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length = 140)
    images = models.ImageField(upload_to="post", blank=True, null=True)
    like_num = models.IntegerField(default=0)

class GoodModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    count = models.IntegerField()

class FollowModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_id = models.IntegerField()

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name="profile")
    introduction = models.TextField(max_length = 140,blank=True, null=True)
    url = models.URLField(max_length=200,blank=True, null=True)
    profile_icon = models.ImageField(upload_to="user",blank=True, default='user/default.png')
