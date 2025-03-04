from django.contrib import admin
from django.urls import path, include  # Добавьте include сюда

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('login/', admin.site.urls),
]
