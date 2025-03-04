from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
from .forms import TableForm
from reservations.models import Reservation

# 📌 API: Создание и получение списка столиков
class TableListCreateView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

# 📌 API: Получение списка доступных столиков на дату
def available_tables(request):
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'Date is required'}, status=400)

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({'error': 'Invalid date format, use YYYY-MM-DD'}, status=400)

    reserved_tables = Reservation.objects.filter(date=date).values_list('table_id', flat=True)
    available = Table.objects.exclude(id__in=reserved_tables)

    return JsonResponse({'available_tables': list(available.values())})

# 📌 HTML: Список столиков
class TableListView(ListView):
    model = Table
    template_name = "tables/table_list.html"
    context_object_name = "tables"

# 📌 HTML: Детали столика
class TableDetailView(DetailView):
    model = Table
    template_name = "tables/table_detail.html"

# 📌 HTML: Создание столика
class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = "tables/table_form.html"
    success_url = reverse_lazy("table_list")

# 📌 HTML: Обновление столика
class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    template_name = "tables/table_form.html"
    success_url = reverse_lazy("table_list")

# 📌 HTML: Удаление столика
class TableDeleteView(DeleteView):
    model = Table
    template_name = "tables/table_confirm_delete.html"
    success_url = reverse_lazy("table_list")
