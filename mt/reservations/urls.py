from django.urls import path
from .views import (
    ReservationListView, ReservationCreateView, ReservationDetailView,
    ReservationUpdateView, ReservationDeleteView
)

urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation_list'),
    path('create/', ReservationCreateView.as_view(), name='reservation_create'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    path('<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),
]
