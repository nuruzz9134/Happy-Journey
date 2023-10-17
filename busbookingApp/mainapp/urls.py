from django.urls import path
from mainapp.views import *

urlpatterns = [
<<<<<<< HEAD
=======
    path('createBus/',CreateBusData.as_view()),
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
    path('buses/',AllBusDatas.as_view()),
    path('search/',SearchedBuses.as_view()),
    path('bookedseats/',BookedBusSeats.as_view()),
    path('seatbook/',ConfirmSeatsBooking.as_view()),
    
<<<<<<< HEAD
=======
    # path('userhistory/',UserBookingHistory.as_view()),
   
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
    path('allnotifications/',ManageNotification.as_view()),
    path('delete_notifications/<int:pk>/',ManageNotification.as_view()),

    path('alltickets/',ManageTickets.as_view()),
    path('delete_tickets/<int:pk>/',ManageTickets.as_view()),
]