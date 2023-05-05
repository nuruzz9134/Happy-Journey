from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django_celery_beat.models import PeriodicTask,CrontabSchedule
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import json
from celery import current_app
from django.db import transaction
import random


User = get_user_model()

routeChoice = [
    ('bankura_durgapur','bnk_dur'),
    ('durgapur_bankura','dur_bnk'),
    ('bankura_karunamoyee','bnk_krnmoy'),
    ('karunamoyee_bankura','krnmoy_bnk'),
    ('durgapur_karunamoyee','dur_krnmoy'),
    ('karunamoyee_durgapur','krnmoy_dur')
]


class BusModel(models.Model):
    number = models.CharField(max_length=15,blank=True,null=True)
    route = models.CharField(max_length= 50 ,choices=routeChoice)
    day = models.CharField(max_length= 250 ,blank=True,null=True)
    time = models.TimeField(blank=True,null=True)
    seats = models.PositiveIntegerField(blank=True,null=True)
    travel_fee = models.PositiveIntegerField(blank=True,null=True)
    photo1 = models.ImageField(upload_to='busImages',blank=True,null=True)
    photo2 = models.ImageField(upload_to='busImages',blank=True,null=True)
    photo3 = models.ImageField(upload_to='busImages',blank=True,null=True)
    photo4 = models.ImageField(upload_to='busImages',blank=True,null=True)
    photo5 = models.ImageField(upload_to='busImages',blank=True,null=True)

    def __str__(self):
        return str(self.id)


class BusBookingModel(models.Model):
    BusTransportDayId = models.CharField(max_length= 100 ,blank=True,null=True)
    UserBookingId = models.CharField(max_length= 100 ,blank=True,null=True)
    bus = models.ForeignKey(BusModel,related_name='busmodel', on_delete=models.CASCADE,blank=True,null=True)
    passenger = models.ForeignKey(User,related_name='passengerID',on_delete=models.CASCADE,blank=True,null=True)
    seat = models.CharField(max_length=250,blank=True,null=True)
    date = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
    
    @staticmethod
    def user_order_details(user_id):
        instance = BusBookingModel.objects.filter(passenger = user_id).first()
        
        data = {}
        data['busid'] = instance.bus_id
        data['passanger'] = instance.passenger_id
        data['bus'] = instance.BusTransportDayId
        data['bookingId'] = instance.UserBookingId
        data['seats'] = instance.seat
        data['date'] = instance.date

        return data

    


class BookedBusSeatsModel(models.Model):
    bus = models.ForeignKey(BusBookingModel,related_name='bookedbusseats', on_delete=models.CASCADE,blank=True,null=True)
    seats = models.CharField(max_length=250,blank=True,null=True)
    available_seats = models.IntegerField(blank=True,null=True)
    date = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id)


class UserNotifications(models.Model):
    user = models.ForeignKey(User,related_name='userID',on_delete=models.CASCADE)
    groupName = models.CharField(max_length=100,blank=True,null=True)
    notifications = models.TextField(max_length=300,blank=True,null=True)
    sent_time = models.DateTimeField(blank=True,null=True)
    sent = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-sent_time']

    def set_periodic_task(self, task_name):
        schedule = self.get_or_create_schedule()
        PeriodicTask.objects.create(
            crontab = schedule, 
            name=f'{self.groupName}<<>>{random.randint(10 , 999900)}',
            task=task_name,
            args=json.dumps(self.user_id),
            kwargs=json.dumps({
                'some_data': self.notifications,
            }),
        )
        print("preiodic........")

    def get_or_create_schedule(self):
        print("crontab........")
        schedule,created= CrontabSchedule.objects.get_or_create(
             
            # hour = self.sent_time.hour,
            # minute = self.sent_time.minute,
            # day_of_month = self.sent_time.day,
            # month_of_year = self.sent_time.month)

            minute='9',
            hour='1',
            day_of_month='29',
            month_of_year='4'
        )
        return schedule


    

# @receiver(post_save,sender = UserNotifications)
# def notification_handeler(sender,instance,created,**kwargs):
#     # call group-send-function directly to send notification or you can creat a dynamic task in celery beats
#     if created:
#         schedule,created= CrontabSchedule.objects.get_or_create(
            # hour = instance.sent_time.hour,
            # minute = instance.sent_time.minute,
            # day_of_month = instance.sent_time.day,
            # month_of_year = instance.sent_time.month)

        #     minute='14',
        #     hour='23',
        #     day_of_month='28',
        #     month_of_year='4'
        #     )
        
        # task = PeriodicTask.objects.create(
        #     crontab = schedule,
        #     name ="broadcast-notification-"+str(instance.id), 
        #     task ="mainapp.tasks.broadcastnotification",
        #     args = json.dumps((instance.id,))
        #     )



@receiver(post_save,sender = UserNotifications)
def set_or_sync_periodic_task(sender, instance=None, created=False, **kwargs):
            if created:
                instance.set_periodic_task(task_name='broadcastnotification')