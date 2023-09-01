from django.db import models
# from account.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Flight(models.Model):
    flight_num = models.CharField(
        max_length=30,
        verbose_name='Номер рейса'
        )
    origin = models.CharField(
        max_length=50,
        verbose_name='Откуда'
        )
    destination = models.CharField(
        max_length=100,
        verbose_name='Куда'
        )
    departure_date = models.DateField(
        verbose_name='Дата вылета'
    )
    departure_time = models.TimeField(
        verbose_name='Времы вылета'
    )
    arrival_date = models.DateField(
        verbose_name='Дата прилета'
    )
    arrival_time = models.TimeField(
        verbose_name='Время прилета'
    )

    def __str__(self):
        return f'Номер рейса {self.flight_num}'
    


class Ticket(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )
    flight = models.ForeignKey(
        Flight, 
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    price = models.DecimalField(
        max_digits=15, 
        decimal_places=2
    )

    def __str__(self):
        return f'{self.user} -> {self.flight}'


class Airplane(models.Model):
    air_name = models.CharField(
        max_length=30
        )
    model_air = models.CharField(
        max_length=30
        )
    seats = models.PositiveIntegerField(unique=True)


    def __str__(self):
        return f'{self.air_name} ({self.model_air})'


class Seat(models.Model):
    airplane = models.ForeignKey(
        Airplane, 
        on_delete=models.CASCADE
        )
    row = models.PositiveIntegerField(
        verbose_name='Ряд'
        )
    seat_num = models.PositiveIntegerField(
        verbose_name='Номер места'
        )
    
    
    def __str__(self):
        return f'Место в {self.airplane} - {self.row} ряд, номер места {self.seat_num}' 
    