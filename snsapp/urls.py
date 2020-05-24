from django.urls import path, include
from .views import aaa

urlpatterns = [
    path('a/', aaa)
]