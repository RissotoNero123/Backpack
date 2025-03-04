from rest_framework import serializers
from .models import Reservation
from tables.models import Table  # Проверь, что импорт правильный

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
