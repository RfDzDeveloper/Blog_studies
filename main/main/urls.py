from django.contrib import admin
from django.urls import path, include
from blog import urls as blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog)),
]
