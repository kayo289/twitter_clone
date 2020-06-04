from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import mypage, signupfunc, loginfunc, index_post,followfunc,follow_delete

#signupfunc, loginfunc, index_post ,
urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('list/',index_post, name='index_post'),
    path('mypage/<int:pk>', mypage,name="mypage"),
    path('follow/<int:pk>',followfunc,name='follow'),
    path('follow_delete/<int:pk>',follow_delete,name='follow_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
