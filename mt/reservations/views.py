from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .models import Reservation, Table, Customer
from .serializers import ReservationSerializer, TableSerializer
from .forms import ReservationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# --- HTML представления ---

# Список всех броней (HTML)
class ReservationListView(ListView):
    model = Reservation
    template_name = "reservations/reservation_list.html"
    context_object_name = "reservations"

# Детали брони (HTML)
class ReservationDetailView(DetailView):
    model = Reservation
    template_name = "reservations/reservation_detail.html"

# Создание брони (HTML)
class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservations/reservation_form.html"
    success_url = reverse_lazy("reservation_list")

# Обновление брони (HTML)
class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservations/reservation_form.html"
    success_url = reverse_lazy("reservation_list")

# Удаление брони (HTML)
class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = "reservations/reservation_confirm_delete.html"
    success_url = reverse_lazy("reservation_list")

# --- API представления ---

# Список всех броней
class ReservationListAPIView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Создание брони с проверкой уникальности
class ReservationCreateAPIView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        customer = request.data.get('customer')
        table = request.data.get('table')
        date = request.data.get('date')

        parsed_date = parse_date(date)
        if not parsed_date:
            return Response({'error': 'Некорректный формат даты'}, status=status.HTTP_400_BAD_REQUEST)

        if Reservation.objects.filter(table=table, date=date).exists():
            return Response({'error': 'Этот стол уже забронирован на указанную дату'}, status=status.HTTP_400_BAD_REQUEST)

        if Reservation.objects.filter(customer=customer, date=date).exists():
            return Response({'error': 'Пользователь уже имеет бронь на этот день'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

# Получение деталей брони
class ReservationDetailAPIView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Получение всех броней пользователя
class UserReservationsAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, user_id):
        customer = get_object_or_404(Customer, id=user_id)
        reservations = Reservation.objects.filter(customer=customer)
        serializer = ReservationSerializer(reservations, many=True)
        return Response({'reservations': serializer.data})

# Обновление статуса брони
class ReservationUpdateAPIView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Удаление брони
class ReservationDeleteAPIView(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Получение списка доступных столиков на указанную дату
class AvailableTablesAPIView(APIView):
    def get(self, request):
        date = request.GET.get('date')
        if not date:
            return Response({'error': 'Дата не указана'}, status=status.HTTP_400_BAD_REQUEST)

        booked_tables = Reservation.objects.filter(date=date).values_list('table', flat=True)
        available_tables = Table.objects.exclude(id__in=booked_tables)
        return Response({'available_tables': TableSerializer(available_tables, many=True).data})

# Получение списка всех столиков
class TableListAPIView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Список всех броней (функция, если нужна)
def reservation_list(request):
    reservations = Reservation.objects.all()
    return JsonResponse({'reservations': list(reservations.values())})
