from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('createBus/',CreateBusData.as_view()),
    path('buses/',AllBusDatas.as_view()),
    path('search/',SearchedBuses.as_view()),
    path('bookedseats/',BookedBusSeats.as_view()),
    path('seatbook/',ConfirmSeatsBooking.as_view()),
    path('userhistory/',UserBookingHistory.as_view()),
    path('seatcancel/',BookingCancel.as_view())
]