from django.urls import path
from .views import (
    TableListView, TableDetailView, TableCreateView, TableUpdateView, TableDeleteView,
    TableListCreateView, available_tables
)

urlpatterns = [
    # HTML маршруты
    path('', TableListView.as_view(), name='table_list'),
    path('<int:pk>/', TableDetailView.as_view(), name='table_detail'),
    path('create/', TableCreateView.as_view(), name='table_create'),
    path('<int:pk>/update/', TableUpdateView.as_view(), name='table_update'),
    path('<int:pk>/delete/', TableDeleteView.as_view(), name='table_delete'),

    # API маршруты
    path('api/', TableListCreateView.as_view(), name='api_table_list_create'),
    path('api/available/', available_tables, name='api_available_tables'),
]
