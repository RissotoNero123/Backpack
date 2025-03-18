from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, Table, Reservation
import json



@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            customer = get_object_or_404(Customer, id=data.get("customer_id"))
            table = get_object_or_404(Table, id=data.get("table_id"))

            # Проверяем, свободен ли столик на эту дату
            if Reservation.objects.filter(table=table, date=data["date"]).exists():
                return JsonResponse({"error": "Table is already reserved for this date"}, status=400)

            # Проверяем, нет ли у клиента брони на эту дату
            if Reservation.objects.filter(customer=customer, date=data["date"]).exists():
                return JsonResponse({"error": "Customer already has a reservation on this date"}, status=400)

            # Создаем бронь
            reservation = Reservation.objects.create(
                customer=customer,
                table=table,
                date=data["date"],
                status="pending"
            )

            # Помечаем столик как занятый
            table.is_available = False
            table.save()

            return JsonResponse({"message": "Reservation created", "id": reservation.id}, status=201)

        except (json.JSONDecodeError, KeyError):
            return JsonResponse({"error": "Invalid request data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def update_reservation_status(request, id):  # Здесь изменил аргумент на id для соответствия urls.py
    if request.method == "PATCH":
        try:
            data = json.loads(request.body)
            reservation = get_object_or_404(Reservation, id=id)

            # Проверяем, есть ли статус в запросе
            if "status" in data:
                reservation.status = data["status"]
                reservation.save()

                # Если бронь отменена, освободим столик
                if data["status"] == "canceled":
                    reservation.table.is_available = True
                    reservation.table.save()

                return JsonResponse({"message": "Reservation status updated"})

            return JsonResponse({"error": "No status provided"}, status=400)

        except (json.JSONDecodeError, KeyError):
            return JsonResponse({"error": "Invalid request data"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
