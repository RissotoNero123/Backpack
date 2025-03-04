from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()  # Добавляем это поле
