from django.urls import path, include
from .views import aaa, signupfunc, loginfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/',loginfunc, name='login'),
]