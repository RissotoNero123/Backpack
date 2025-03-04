from django.shortcuts import render, get_object_or_404
from .models import Customer
from rest_framework import generics
from .serializers import CustomerSerializer

# HTML-страницы
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/list.html', {'customers': customers})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customers/detail.html', {'customer': customer})

# API-представления
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
