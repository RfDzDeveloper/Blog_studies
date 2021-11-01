from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('read_posts/', views.read_posts, name='read_posts'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name="regiter"),
    path('logout', views.logout_view, name='logout'),
    path('add_post', views.add_post, name='add_post'),
    path('delete_post', views.delete_post, name='delete_post'),
    path('my_all_posts', views.view_user_post, name='view_user_post'),
]