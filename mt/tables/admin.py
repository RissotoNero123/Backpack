from django.contrib import admin
from .models import Table
from customers.models import Customer
from reservations.models import Reservation


admin.site.register(Table)
