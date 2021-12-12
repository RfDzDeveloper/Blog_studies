from django import views
from django.contrib import admin
from django.urls import path, include
from blog import urls as blog
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog)),
    path('', views.home, name='home'),
]
