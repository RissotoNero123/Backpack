from django.urls import path
from .views import create_reservation, reservation_detail, update_reservation_status

urlpatterns = [
    path("", create_reservation),
    path("<int:id>/", reservation_detail),
    path("<int:id>/update/", update_reservation_status),
]
