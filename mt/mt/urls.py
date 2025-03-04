from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('tables/', include('tables.urls')),
    path('reservations/', include('reservations.urls')),  # Оставляем только одну строку
]
