# blog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import PostViewSet, CommentViewSet

# ██████╗ ██████╗ ███████╗████████╗ ██████╗ 
# ██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗
# ██████╔╝██████╔╝█████╗     ██║   ██║   ██║
# ██╔═══╝ ██╔══██╗██╔══╝     ██║   ██║   ██║
# ██║     ██║  ██║███████╗   ██║   ╚██████╔╝
# ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ 

# 1. Основной роутер для постов
#    Создает стандартные CRUD endpoints для PostViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# 2. Вложенный роутер для комментариев
#    Создает endpoints вида: /posts/{post_id}/comments/
posts_router = routers.NestedDefaultRouter(
    parent_router=router,          # родительский роутер
    parent_prefix=r'posts',        # префикс родителя
    lookup='post'                  # название параметра для post_id
)
posts_router.register(
    prefix=r'comments',            # префикс для комментариев
    viewset=CommentViewSet,        # viewset для обработки
    basename='post-comments'       # имя для reverse URL
)

# 3. Объединение всех URL-путей
urlpatterns = [
    # ██████╗  ██████╗ ████████╗███████╗
    # ██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝
    # ██████╔╝██║   ██║   ██║   ███████╗
    # ██╔═══╝ ██║   ██║   ██║   ╚════██║
    # ██║     ╚██████╔╝   ██║   ███████║
    # ╚═╝      ╚═════╝    ╚═╝   ╚══════╝
    # 
    # Доступные endpoints:
    # - GET, POST       /api/posts/
    # - GET, PUT, PATCH, DELETE /api/posts/{pk}/
    path('', include(router.urls)),
    
    # ██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗ 
    # ██║  ██║██║   ██║██╔══██╗██╔════╝██╔══██╗
    # ███████║██║   ██║██████╔╝█████╗  ██████╔╝
    # ██╔══██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗
    # ██║  ██║╚██████╔╝██║     ███████╗██║  ██║
    # ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝
    # 
    # Доступные endpoints:
    # - GET, POST       /api/posts/{post_pk}/comments/
    # - GET, PUT, PATCH, DELETE /api/posts/{post_pk}/comments/{pk}/
    path('', include(posts_router.urls)),
]