from django.urls import path
from .views import (
    customer_list, customer_detail, 
    CustomerListCreateView, CustomerDetailView
)

urlpatterns = [
    # HTML-страницы
    path('', customer_list, name='customer-list'),
    path('<int:id>/', customer_detail, name='customer-detail'),
    
    # API
    path('api/', CustomerListCreateView.as_view(), name='customer-api-list'),
    path('api/<int:pk>/', CustomerDetailView.as_view(), name='customer-api-detail'),
]
