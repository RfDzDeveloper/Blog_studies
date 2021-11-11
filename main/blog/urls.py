from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_world/', views.my_home, 'my_home'),
    path('read_posts/<int:post_id>', views.read_post, name='read_post'),
    path('view_all_posts/', views.view_all_posts, name='view_all_posts'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name='logout'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/', views.edit_post, name='edit_post'),
    path('delete_post/', views.delete_post, name='delete_post'),
    path('my_all_posts/', views.view_user_post, name='view_user_post'),
]