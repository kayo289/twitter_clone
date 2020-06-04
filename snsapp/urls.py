from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import signupfunc, loginfunc, index_post, profile_edit

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
    path('list/',index_post, name='index_post'),
    path('profile-edit/<int:pk>', profile_edit.as_view(),name = 'profile-edit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)