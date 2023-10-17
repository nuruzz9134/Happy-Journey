# Generated by Django 4.1.6 on 2023-07-27 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=15, null=True)),
                ('route', models.CharField(choices=[('bankura_durgapur', 'bnk_dur'), ('durgapur_bankura', 'dur_bnk'), ('bankura_karunamoyee', 'bnk_krnmoy'), ('karunamoyee_bankura', 'krnmoy_bnk'), ('durgapur_karunamoyee', 'dur_krnmoy'), ('karunamoyee_durgapur', 'krnmoy_dur')], max_length=50)),
                ('day', models.CharField(blank=True, max_length=250, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('seats', models.PositiveIntegerField(blank=True, null=True)),
                ('travel_fee', models.PositiveIntegerField(blank=True, null=True)),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='busImages')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='busImages')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='busImages')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='busImages')),
                ('photo5', models.ImageField(blank=True, null=True, upload_to='busImages')),
            ],
        ),
        migrations.CreateModel(
            name='UserNotifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(blank=True, max_length=100, null=True)),
                ('notifications', models.TextField(blank=True, max_length=300, null=True)),
                ('sent_time', models.DateTimeField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userID', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-sent_time'],
            },
        ),
        migrations.CreateModel(
            name='BusBookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BusTransportDayId', models.CharField(blank=True, max_length=100, null=True)),
                ('UserBookingId', models.CharField(blank=True, max_length=100, null=True)),
                ('seat', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('bus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='busmodel', to='mainapp.busmodel')),
                ('passenger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passengerID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookedBusSeatsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.CharField(blank=True, max_length=250, null=True)),
                ('available_seats', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('bus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookedbusseats', to='mainapp.busbookingmodel')),
            ],
        ),
    ]