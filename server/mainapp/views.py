from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
import datetime
import time
from datetime import timedelta
from django.db.models import Q
from .models import *
from .serializer import *
from .models import User



class CreateBusData(APIView):
    def post(self,request):
        try:
            serializer = BusModelSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msz": "Bus Created successfully."}, status=HTTP_201_CREATED)
            else:
                return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msz": str(e)}, status=HTTP_400_BAD_REQUEST)
        


class AllBusDatas(APIView):
    def get(self,request):
        data = BusModel.objects.all()
        serializer = BusModelSerializer(data,many=True)
        return Response(serializer.data)
    


class SearchedBuses(APIView):
    def get(self,request):
        try:
            fromm = request.query_params.get("from",'')
            to = request.query_params.get('to','')
            searched_day = request.query_params.get('day','')
            searched_date = request.query_params.get('date','')

            query = fromm + "_" + to

           
            data = BusModel.objects.filter(
                Q(Q(route__icontains=query))
                )
            
            days=[]
            for i in data:
                spliting = i.day.split(',')
                for j in spliting:
                    if j not in days:
                        days.append(j)

            flag = False
            for day in days:
                if day == searched_day:
                    flag = True
            if flag == False:
                    return Response({"msz": "bus is not available in that day"}, status=HTTP_400_BAD_REQUEST)
            else:
                buses=[]
                for i in data:
                    obj ={}
                    obj={
                        "id":i.id,
                        "number":i.number,
                        "route":i.route,
                        "day":i.day,
                        "time":i.time,
                        "seats":i.seats,
                        "travel_fee":i.travel_fee
                        }
                    obj.update({'date':searched_date})
                buses.append(obj)
            return Response({"msz":buses}, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({"msz": str(e)}, status=HTTP_400_BAD_REQUEST)



class ConfirmSeatsBooking(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        try:
            busid =request.data['busid'] 
            transportbusid = request.data['busTransportDayId']
            seats = request.data['seats']
            date = request.data['date']
            userid = request.user.id

            bookingDate = datetime.datetime.strptime(date,"%Y-%m-%d")
            currDateString = datetime.datetime.now().strftime("%Y-%m-%d")
            currDate = datetime.datetime.strptime(currDateString,"%Y-%m-%d")
        
            dayDiff = (bookingDate - currDate).days

            if dayDiff > 7 or dayDiff < 0:
                return Response({'msg':'your date is exceeded'}, status=HTTP_400_BAD_REQUEST)
            else:
                available = True
                if dayDiff == 0:
                    currTime = datetime.datetime.now().time()
                    bus_time = BusModel.objects.get(id =busid).time
                    if bus_time < currTime:
                        available = False
                if available == False:
                    return Response({'msg':'bus already leave from depo'}, status=HTTP_400_BAD_REQUEST)
                else:
                    if BusModel.objects.filter(id=busid).exists():

                        splitOrderedseats = str(seats).split(' ')
                        numberOForderedseats = 0
                        for i in splitOrderedseats:
                            if i != '':
                                numberOForderedseats += 1


                        if BusBookingModel.objects.filter(BusTransportDayId = transportbusid).exists():
                            id = BusBookingModel.objects.filter(BusTransportDayId = transportbusid).first().id
                            bookedseats = BookedBusSeatsModel.objects.filter(bus=id).first().seats
                            totalbookedseats = BookedBusSeatsModel.objects.filter(bus=id).first().available_seats

                            splitBookedseats = bookedseats.split(' ')
                            availableSeats = totalbookedseats - numberOForderedseats

                            newbookedSeats = ''
                            seatExist = False
                            for i in range(len(splitBookedseats)):
                                for j in range(len(splitOrderedseats)):
                                    if bookedseats[i] == splitOrderedseats[j]:
                                        seatExist = True
                                        break
                            if seatExist == True:
                                return Response({'msg':'seat already booked'}, status=HTTP_400_BAD_REQUEST)
                            else:
                                newbookedSeats = bookedseats + seats
                                user = User.objects.get(id=userid)

                                existedPassengerseat = BusBookingModel.objects.filter(bus_id = busid,
                                                                  BusTransportDayId = transportbusid,
                                                                  date = date)
                                if existedPassengerseat.exists():
                                    passangerseats = existedPassengerseat.first().seat
                                    newpassangerseats = passangerseats + seats
                                    BusBookingModel.objects.update(
                                    seat = newpassangerseats
                                    )
                                else:
                                    BusBookingModel.objects.create(
                                    bus_id = busid,
                                    BusTransportDayId = transportbusid,
                                    passenger = user,
                                    seat = seats,
                                    date = date
                                    )
                        
                                id = BusBookingModel.objects.filter(BusTransportDayId = transportbusid).first().id
                                BookedBusSeatsModel.objects.update(
                                bus_id=id,
                                seats = newbookedSeats,
                                available_seats = availableSeats,
                                date = date
                                    )
                                return Response ({'msg' :'seat booked','user':userid}, status=HTTP_201_CREATED)


                        else:
                            user = User.objects.get(id=userid)
                            BusBookingModel.objects.create(
                                bus_id = busid,
                                BusTransportDayId = transportbusid,
                                passenger = user,
                                seat = seats,
                                date = date
                                )
                            id = BusBookingModel.objects.filter(BusTransportDayId = transportbusid).first().id
                            availableSeats =( 40 - numberOForderedseats)
                            BookedBusSeatsModel.objects.create(
                                bus_id = id,
                                seats = seats,
                                available_seats = availableSeats,
                                date = date
                                )
                            return Response ({'msg' :'seat booked'}, status=HTTP_201_CREATED)


                    else:
                        return Response ({'msg' : "bus does not find"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({str(e)}, status=HTTP_400_BAD_REQUEST)
        


class BookedBusSeats(APIView):
    def get(self,request):
        searched_bus = request.query_params.get('id','')
        searched_date = request.query_params.get('date','')
        
        try:
            if BusBookingModel.objects.filter(BusTransportDayId=searched_bus,date=searched_date).exists():
                busid = BusBookingModel.objects.filter(BusTransportDayId=searched_bus,date=searched_date).first().id
                seats = BookedBusSeatsModel.objects.filter(bus = busid).first().seats
                print("seats", seats)
                bookedseatsList = seats.split(' ')
                print(bookedseatsList)
                return Response ({'seats':bookedseatsList}, status=HTTP_201_CREATED)
            else:
                return Response ({'seats':None}, status=HTTP_201_CREATED)
        except Exception as e :
            return Response({str(e)}, status=HTTP_400_BAD_REQUEST)
        

        
class UserBookingHistory(APIView):
    def get(self,request):
        try:
            userid = request.user.id
            data = BusBookingModel.objects.filter(passenger = userid)
            serializer = BookingModelSerializer(data,many=True)
            print(">>>>>",serializer.data)
            return Response ({'msg': serializer.data}, status=HTTP_201_CREATED)
        except Exception as e :
            return Response({str(e)}, status=HTTP_400_BAD_REQUEST)
        

class BookingCancel(APIView):
    def put(self,request):
        try:
            userid = request.user.id
            busid = request.data['b_id']
            seatNumber = request.data['seat']
            date = request.data['date']

            bookedSeats = BusBookingModel.objects.filter(
                                    passenger = userid,
                                    BusTransportDayId=busid,
                                    date=date).first().seat
            newSeats = ''
            for i in  bookedSeats.split(' '):
                if i != str(seatNumber):
                    newSeats = newSeats + i + ' '
            BusBookingModel.objects.update(seat = newSeats)

            bookedbusId = BusBookingModel.objects.filter(BusTransportDayId = busid).first().id
            seats = BookedBusSeatsModel.objects.filter(bus_id = bookedbusId).first().seats

            updateSeats = ''
            for j in  seats.split(' '):
                if j != str(seatNumber):
                    updateSeats = updateSeats + j + ' '
            BookedBusSeatsModel.objects.filter(bus_id = bookedbusId).update(seats = updateSeats)
            return Response ({'msg': 'updated'}, status=HTTP_201_CREATED)
        
        except Exception as e :
            return Response({str(e)}, status=HTTP_400_BAD_REQUEST)
        

# class NotificationSend(APIView):

        
