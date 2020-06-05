from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import mypage, signupfunc, loginfunc, index_post,followfunc,follow_delete,goodfunc,create_posts,logoutfunc,search
from . import views

#signupfunc, loginfunc, index_post ,
urlpatterns = [
    path('', search, name='search'),
    path('signup/', signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('logout/',logoutfunc, name='logout'),
    path('list/',index_post, name='index_post'),
    path('mypage/<int:pk>', mypage,name="mypage"),
    path('follow/<int:pk>',followfunc,name='follow'),
    path('follow_delete/<int:pk>',follow_delete,name='follow_delete'),
    path('good/<int:pk>',goodfunc,name='good'),
    path('create/', create_posts.as_view(), name="create"),
]

