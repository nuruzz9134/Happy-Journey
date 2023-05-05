from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from .models import *
import datetime
# from datetime import timedelta
import json
from asgiref.sync import async_to_sync,sync_to_async
from channels.db import database_sync_to_async


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["userId"]
        self.room_group_name = "user_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        print("room>>>>",self.room_name)

        await self.accept()
        print("websocket connected........")


        booking_detailed = await sync_to_async(BusBookingModel.user_order_details)(self.room_name)
        
        date = booking_detailed['date']
        dt = datetime.datetime.strftime(date,"%d/%m/%Y")
        b_id = booking_detailed['busid']
        passanger = booking_detailed['passanger']

        passangerName = await database_sync_to_async(User.objects.get)(id=passanger)
        name = passangerName.name
        busNumber = await database_sync_to_async(BusModel.objects.get)(id=b_id)
        number = busNumber.number
        time = busNumber.time
        t = datetime.time.strftime(time,"%H:%M:%S")

        msg = {}
        msg['passangerNmae'] = name
        msg['bus'] = booking_detailed['bus']
        msg['busNumber'] = number
        msg['busTime'] = t
        msg['bookingId'] = booking_detailed['bookingId']
        msg['seats'] = booking_detailed['seats']
        msg['date'] = dt
        

        # await self.send(text_data = json.dumps({
        #     'payload' : msg
        # }))

        date_time_str = dt +' '+ t
        dateTime = datetime.datetime.strptime(date_time_str,"%d/%m/%Y %H:%M:%S")
        print(dateTime)
        print(type(dateTime))


        busNumber = await database_sync_to_async(UserNotifications.objects.create)(
                                                        user_id = self.room_name,
                                                        groupName = self.room_group_name,
                                                        notifications = msg,
                                                        sent_time = dateTime)


    async def send_notification(self, event):
            print(event)
            message = event["message"]
            # text_data=json.dumps(message)
            text_data = message
            print(text_data)

            # Send message to WebSocket
            await self.send(text_data)
            print("data send to script")




    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )