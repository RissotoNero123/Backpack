from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} ({'Available' if self.is_available else 'Occupied'})"

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reservations")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations")
    date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Reservation for {self.customer.name} on {self.date}"
