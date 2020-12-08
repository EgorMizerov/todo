from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    # path(r'$', views.test, name='login'),
]
