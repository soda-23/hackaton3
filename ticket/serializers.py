from rest_framework import serializers
from .models import Airplane, Seat, Flight, Ticket
from datetime import datetime


class AirplaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplane
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

    def validate(self, data):
        flight = data.get('flight')
        departure_datetime = datetime.combine(flight.departure_date, flight.departure_time)
        created_at = data.get('created_at')

        if created_at > departure_datetime:
            raise serializers.ValidationError('Билет невозможно приобрести после вылета рейса')
            
        return serializers.data



class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = '__all__'


    def validate(self, data):
        airplane = data.get('airplane')
        row = data.get('row')
        seat_num = data.get('seat_num')

        if Seat.objects.filter(airplane=airplane, row=row, seat_num=seat_num).exists():
            raise serializers.ValidationError('Это место уже занято')
        
        return serializers.data


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'

    
    def validate(self, data):
        flight_number = data.get('flight_number')
        
        if Flight.objects.filter(flight_number=flight_number).exists():
            raise serializers.ValidationError('Такой рейс уже существует')
        
        return serializers.data