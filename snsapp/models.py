from django.db import models

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
