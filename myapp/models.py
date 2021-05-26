from django.db import models
from rest_framework.fields import FileField

alarm_choices = (
     ('1','VIBRATION'), ('2','OVERSPEED'), ('3','CRASH'), ('4','HARD_ACCELERATION'), ('5','HARD_BRAKE'),
('6','SHARP_TURN')
)

command_choices = (
    ('1','Reboot'),('2','Configure ip:port')
)

response_choice = (
    ('1','OK'),('2','Failure')
)

class Login(models.Model):
    type = models.CharField(max_length=10)
    imei = models.CharField(primary_key = True,max_length=30)

    def __str__(self):
        return self.imei

class Alarm_messege(models.Model):
    imei = models.ForeignKey('Login',on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    alarm_type = models.CharField(choices = alarm_choices, max_length=10)
    alarm_time = models.DateTimeField(verbose_name =("alarm-time"), auto_now=True)  #
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    file_list = models.CharField(max_length=30) #

    def __str__(self):
        return self.type

class Location_messege(models.Model):
    imei = models.ForeignKey('Login',on_delete=models.CASCADE) 
    type = models.CharField(max_length=10)
    location_time = models.DateTimeField(verbose_name =("location-time"), auto_now=True)  #
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Videos(models.Model):
    imei = models.ForeignKey('Login',on_delete=models.CASCADE) 
    video = models.FileField()
    video_data = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.video_data

class Command_msg(models.Model):
    type = models.CharField(max_length=10)
    imei = models.ForeignKey('Login',on_delete=models.CASCADE) 
    command_type = models.CharField(choices = command_choices, max_length=20)

    def __str__(self):
        return self.type

class command_Response(models.Model):
    imei = models.ForeignKey('Login',default = '0',on_delete=models.CASCADE) 
    type = models.CharField(max_length=20, default='COMMAND_RESPONSE')
    response = models.CharField(choices = response_choice, max_length=20)
   
    def __str__(self):
        return self.type

# Create your models here.
