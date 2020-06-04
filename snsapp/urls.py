from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import signupfunc, loginfunc, index_post
from . import views

app_name ='blog'

urlpatterns = [
path('signup/', signupfunc, name='signup'),
path('login/',loginfunc, name='login'),
path('list/',index_post, name='index_post'),
path('', views.index, name='index'),
path('detail/<int:blog_id>/', views.detail, name='detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
