from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import signupfunc, loginfunc, index_post

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('list/',index_post, name='index_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)