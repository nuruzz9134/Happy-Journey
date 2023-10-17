from django.contrib import admin
<<<<<<< HEAD
from mainapp.models import *

# Register your models here.


@admin.register(BusModel)
class BusModeladmin(admin.ModelAdmin):
    list_display = [
        field.name for field in BusModel._meta.fields
        ]
    
@admin.register(BusBookingModel)
class BusBookingModeladmin(admin.ModelAdmin):
    list_display = [
        field.name for field in BusBookingModel._meta.fields
        ]
    
@admin.register(BookedBusSeatsModel)
class BookedBusSeatsModeladmin(admin.ModelAdmin):
    list_display = [
        field.name for field in BookedBusSeatsModel._meta.fields
        ]
    
@admin.register(UserNotifications)
class UserNotificationsModeladmin(admin.ModelAdmin):
    list_display = [
        field.name for field in UserNotifications._meta.fields
        ]
=======
# from .models import BusModel,BusBookingModel,BookedBusSeatsModel,UserNotifications

# # Register your models here.
# @admin.register()
# class BusModeladmin(admin.ModelAdmin):
#     list_display = [
#         field.name for field in BusModel._meta.fields
#         ]
    
# @admin.register()
# class BusBookingModeladmin(admin.ModelAdmin):
#     list_display = [
#         field.name for field in BusBookingModel._meta.fields
#         ]
    
# @admin.register()
# class BookedBusSeatsModeladmin(admin.ModelAdmin):
#     list_display = [
#         field.name for field in BookedBusSeatsModel._meta.fields
#         ]
    
# @admin.register()
# class UserNotificationsModeladmin(admin.ModelAdmin):
#     list_display = [
#         field.name for field in UserNotifications._meta.fields
#         ]
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
