from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('read_posts', views.read_posts, name='read_posts'),
]