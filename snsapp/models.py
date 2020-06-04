from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length = 140)
    images = models.ImageField(upload_to="post", blank=True, null=True)
    like_num = models.IntegerField(default=0)

    def __str__(self):
        return self.content

class GoodModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    count = models.IntegerField()

class FollowModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_id = models.IntegerField()

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name="profile")
    introduction = models.TextField(max_length = 140)
    url = models.URLField(max_length=200)
    profile_icon = models.ImageField(upload_to="user")

class Blog(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('テキスト')
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'
