# myblog/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from blog.views import PostViewSet, CommentViewSet

# ██████╗ ██╗   ██╗██████╗ ██╗     ███████╗
# ██╔══██╗██║   ██║██╔══██╗██║     ██╔════╝
# ██████╔╝██║   ██║██████╔╝██║     █████╗  
# ██╔══██╗██║   ██║██╔══██╗██║     ██╔══╝  
# ██║  ██║╚██████╔╝██████╔╝███████╗███████╗
# ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝

# 1. Базовый роутер для постов
#    Создает стандартные CRUD endpoints:
#    - /posts/       (GET, POST)
#    - /posts/{pk}/  (GET, PUT, PATCH, DELETE)
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# 2. Вложенный роутер для комментариев
#    Создает endpoints вида:
#    - /posts/{post_pk}/comments/       (GET, POST)
#    - /posts/{post_pk}/comments/{pk}/  (GET, PUT, PATCH, DELETE)
posts_router = routers.NestedDefaultRouter(
    parent_router=router,
    parent_prefix=r'posts',
    lookup='post'  # имя параметра для post_pk в URL
)
posts_router.register(
    prefix=r'comments',
    viewset=CommentViewSet,
    basename='post-comments'
)

# ██╗   ██╗██████╗ ██╗     ███████╗███████╗
# ██║   ██║██╔══██╗██║     ██╔════╝██╔════╝
# ██║   ██║██████╔╝██║     █████╗  ███████╗
# ██║   ██║██╔═══╝ ██║     ██╔══╝  ╚════██║
# ╚██████╔╝██║     ███████╗███████╗███████║
#  ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚══════╝

urlpatterns = [
    # Админ-панель Django
    path('admin/', admin.site.urls),
    
    # API аутентификация (для браузерного API)
    path('api-auth/', include('rest_framework.urls')),
    
    # Основные API endpoints
    # Включаем оба роутера в корень проекта
    path('', include(router.urls)),          # Посты
    path('', include(posts_router.urls)),    # Комментарии
    
    # Дополнительные API endpoints из blog/urls.py
    path('api/', include('blog.urls')),
    
    # Можно добавить здесь другие приложения
    # path('users/', include('users.urls')),
]