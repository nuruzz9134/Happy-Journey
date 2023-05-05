
from celery import shared_task
from busbookingApp.celery import app
from channels.layers import get_channel_layer
from celery import Celery,states
from celery.exceptions import Ignore

from asgiref.sync import async_to_sync
import asyncio
import json
from .models import UserNotifications


# @app.task(name='project_tasks')
# @app.task()

@shared_task(bind = True)
def broadcastnotification(data):
    print("Task data : ",data)
    notification = UserNotifications.objects.filter(id = int(data))
    if len(notification)>0:
            notification = notification.first()
            groupname = notification.groupName
            channel_layer = get_channel_layer()

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(channel_layer.group_send(
            groupname,
            {
            'type':'send_notification',
            'message': json.dumps(notification.notifications),
            })
            )
            notification.sent = True
            notification.save()
            return 'Done'



# @shared_task(bind = True)
# def broadcastnotification(self,data):
#     print("Task data : ",data)
#     try:
#         notification = UserNotifications.objects.filter(id = int(data))
#         if len(notification)>0:
#             notification = notification.first()
#             groupname = notification.groupName
#             channel_layer = get_channel_layer()

#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             loop.run_until_complete(channel_layer.group_send(
#             groupname,
#             {
#             'type':'send_notification',
#             'message': json.dumps(notification.notifications),
#             })
#             )
#             notification.sent = True
#             notification.save()
#             return 'Done'
        
#         else:
#             self.update_state(
#                 state = 'Failure',
#                 meta = {"exe":"Not Found"},
#                 )
#             raise Ignore()


#     except:
#         self.update_state(
#                 state = 'Failure',
#                 meta = {"exe":"Not Found"},
#                 )
#         raise Ignore()
    
