from django.urls import path
from .views import(
    ticket_list,
    airplane_list,
    seat_list,
    flight_list,
    
)


urlpatterns = [
    path('airplane/', airplane_list),
    path('ticket/', ticket_list),
    path('seat/', seat_list),
    path('flight/', flight_list),
]