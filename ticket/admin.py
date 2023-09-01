from django.contrib import admin
from .models import Airplane, Seat, Flight, Ticket

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Seat)
admin.site.register(Airplane)
admin.site.register(Flight)
