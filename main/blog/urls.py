from django.urls import path
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
    path('add_comment/', views.add_comment, name='add_comment'),
    path('edit_comment/', views.edit_comment, name='edit_comment'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<str:token>/', views.reset_password, name='reset_password'),
    path('success_reset_password/', views.success_reset_password, name="successful_reset_password"),    
    path('change_password/', views.change_password, name='change_password'),
    path('add_rating/', views.add_ratings, name='add_rating'),
]