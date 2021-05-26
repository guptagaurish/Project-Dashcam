from rest_framework import serializers
from .models import Login , Alarm_messege, Location_messege, Videos, Command_msg, Videos, alarm_choices, command_Response,command_choices

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['type', 'imei',]

class AlarmmsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm_messege
        fields = '__all__'

class LocationmsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location_messege
        fields = '__all__'

class VideouploadmsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class CommandmsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command_msg
        fields = '__all__'

class CommandresponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = command_Response
        fields = '__all__'