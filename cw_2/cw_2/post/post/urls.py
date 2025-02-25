from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
