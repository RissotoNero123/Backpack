from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # ✅ Добавлено
from .models import Table
import json

@csrf_exempt
def table_list(request):
    tables = list(Table.objects.values())
    return JsonResponse(tables, safe=False)

@csrf_exempt
def table_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            table = Table.objects.create(number=data["number"], seats=data["seats"])
            return JsonResponse({"id": table.id, "number": table.number, "seats": table.seats}, status=201)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({"error": "Invalid data"}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def available_tables(request):
    available_tables = list(Table.objects.filter(is_available=True).values())
    return JsonResponse(available_tables, safe=False)
