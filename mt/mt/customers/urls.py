from django.urls import path
from .views import customer_list, customer_detail

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('<int:id>/', customer_detail, name='customer_detail'),
]
