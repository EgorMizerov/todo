from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', 'django.contrib.auth.views.login', name='login'),
    path('logout/', 'django.contrib.auth.views.logout', name='login'),
]
