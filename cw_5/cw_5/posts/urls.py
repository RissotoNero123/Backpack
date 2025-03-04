from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('my/', views.my_posts, name='my_posts'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:id>/delete/', views.delete_post, name='delete_post'),
]
