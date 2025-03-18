from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def customer_list(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        return render(request, "customers/list.html", {"customers": customers})  # Отображаем HTML-шаблон
    elif request.method == "POST":
        data = json.loads(request.body)
        customer = Customer.objects.create(name=data["name"], phone=data["phone"])
        return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, pk=id)
    return render(request, "customers/detail.html", {"customer": customer})  # Отображаем HTML-шаблон
