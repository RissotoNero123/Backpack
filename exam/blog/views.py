# blog/views.py

from django.contrib.auth.models import User
from rest_framework import viewsets, filters, generics, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, RegisterSerializer
from .permissions import IsOwnerOrReadOnly

# ███████╗███████╗██████╗ ██╗██████╗ ███████╗██████╗ 
# ██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
# ███████╗█████╗  ██████╔╝██║██████╔╝█████╗  ██████╔╝
# ╚════██║██╔══╝  ██╔══██╗██║██╔══██╗██╔══╝  ██╔══██╗
# ███████║███████╗██║  ██║██║██║  ██║███████╗██║  ██║
# ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

class RegisterView(generics.CreateAPIView):
    """
    █▀█ █▀▀ █▀▀ █▀▀ █▀▀ █▀█ █▀▄▀█ █▀█ 
    █▀▄ ██▄ █▀░ ██▄ ██▄ █▀▄ █░▀░█ █▄█

    Endpoint: POST /api/register/
    Позволяет зарегистрировать нового пользователя.
    Доступен без аутентификации.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


# ██████╗  ██████╗ ████████╗███████╗
# ██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝
# ██████╔╝██║   ██║   ██║   ███████╗
# ██╔═══╝ ██║   ██║   ██║   ╚════██║
# ██║     ╚██████╔╝   ██║   ███████║
# ╚═╝      ╚═════╝    ╚═╝   ╚══════╝

class PostViewSet(viewsets.ModelViewSet):
    """
    █▀█ █▀▀ █▀ ▀█▀ █▀█ █▀▀ █▀▀ █▀ 
    █▀▄ ██▄ ▄█ ░█░ █▄█ ██▄ █▄▄ ▄█

    Полный CRUD для постов:
    - GET    /api/posts/       - список всех постов
    - POST   /api/posts/       - создать новый пост
    - GET    /api/posts/{id}/  - получить пост
    - PUT    /api/posts/{id}/  - обновить пост
    - PATCH  /api/posts/{id}/  - частично обновить пост
    - DELETE /api/posts/{id}/  - удалить пост

    Требуется аутентификация.
    Только владелец может изменять/удалять пост.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        """Автоматически устанавливает автора поста"""
        serializer.save(author=self.request.user)


# █▀▀ █▀▀ █▀█ █▀▀ █▀▀ █░░ █▀█ █▀▀ █▀▀ █▀ 
# █▀░ ██▄ █▀▄ ██▄ ██▄ █▄▄ █▄█ ██▄ █▄▄ ▄█

class CommentViewSet(viewsets.ModelViewSet):
    """
    █▀▀ █▀▀ █▀█ █▀▀ █▀▀ █░░ █▀█ █▀▀ █▀▀ █▀ 
    █▀░ ██▄ █▀▄ ██▄ ██▄ █▄▄ █▄█ ██▄ █▄▄ ▄█

    Полный CRUD для комментариев:
    - GET    /api/posts/{id}/comments/       - список комментариев
    - POST   /api/posts/{id}/comments/       - добавить комментарий
    - GET    /api/posts/{id}/comments/{id}/  - получить комментарий
    - PUT    /api/posts/{id}/comments/{id}/  - обновить комментарий
    - PATCH  /api/posts/{id}/comments/{id}/  - частично обновить
    - DELETE /api/posts/{id}/comments/{id}/  - удалить комментарий

    Требуется аутентификация.
    Только владелец может изменять/удалять комментарий.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """Фильтрация комментариев по ID поста"""
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post__pk=post_id).order_by('created_at')

    def perform_create(self, serializer):
        """Автоматически привязывает комментарий к посту и автору"""
        post = Post.objects.get(pk=self.kwargs.get('post_pk'))
        serializer.save(
            author=self.request.user,
            post=post
        )
