from django.contrib import admin
from .models import  Login , Alarm_messege, Location_messege, Videos, Command_msg, command_Response
 
admin.site.register(Login)
admin.site.register(Alarm_messege)
admin.site.register(Location_messege)
admin.site.register(Videos)
admin.site.register(Command_msg)
admin.site.register(command_Response)

# Register your models here.
