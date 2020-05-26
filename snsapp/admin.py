from django.contrib import admin
from .models import PostModel,GoodModel,FollowModel,IntoroductionModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(GoodModel)
admin.site.register(FollowModel)
admin.site.register(IntoroductionModel)