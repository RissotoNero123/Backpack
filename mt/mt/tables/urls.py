from django.urls import path
from .views import table_list, table_create, available_tables

urlpatterns = [
    path("", table_list),
    path("available/", available_tables),
    path("create/", table_create),
]
