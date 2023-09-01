from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Ticket, Airplane, Seat, Flight
from .serializers import TicketSerializer, FlightSerializer, SeatSerializer, AirplaneSerializer
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def ticket_list(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=200)
    


@api_view(['GET', 'POST'])
def flight_list(request):
    if request.method == 'GET':
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    


@api_view(['GET', 'POST'])
def seat_list(request):
    if request.method == 'GET':
        seats = Seat.objects.all()
        serializer = SeatSerializer(seats, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'POST'])
def airplane_list(request):
    if request.method == 'GET':
        airplane = Airplane.objects.all()
        serializer = AirplaneSerializer(airplane, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AirplaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)