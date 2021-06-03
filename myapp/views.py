from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.generic import ListView
from .models import *
from .serializers import *
from django.db.models import Q

@api_view(['GET', 'POST'])
def Login_get(request):
    if request.method == 'GET':
        Logindata = Login.objects.all()
        serializer = LoginSerializer(Logindata, many=True)
        return Response(serializer.data)

    if request.method == 'POST': 

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Alarmdata_get(request,imei):
   
        try:
           Alarmmsgdata = Alarm_messege.objects.filter('imei') #
        except Alarm_messege.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
           serializer = AlarmmsgSerializer(Alarmmsgdata, many=True)
           return Response(serializer.data)

        if request.method == 'POST': 

            serializer = AlarmmsgSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Locdata_get(request,imei):
   
        try:
           Locmsgdata = Location_messege.objects.filter('imei') #
        except Location_messege.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
           serializer = LocationmsgSerializer(Locmsgdata, many=True)
           return Response(serializer.data)

        if request.method == 'POST': 

            serializer = LocationmsgSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['POST'])
def upload_video(request):
     
    if request.method == 'POST': 

        serializer = VideouploadmsgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
        '''video_data = request.POST['video_data']
        video = request.POST['video']
         
        content = Videos(video_data=video_data,video=video)
        content.save()
        return redirect('home')
     
    return render(request,'upload.html')'''
 
 

class Command_get(APIView):
   

    def get(self, request, format=None):
        Commandmsgdata = Command_msg.objects.all()
        serializer = AlarmmsgSerializer(Commandmsgdata, many=True)
        return Response(serializer.data)

class Commandresponse_get(APIView):
   

    def post(self, request, format=None):
        serializer = CommandresponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


def display(request):
    if request.method == "GET":
        videos = Videos.objects.all()
        context ={
            'videos':videos,
        }
     
        return render(request,'videos.html',context)

def fetch_alarmby_type(request):
    if request.method == "GET":
        queryset = Alarm_messege.objects.filter(
         alarm_type = input()
        ).values('imei','type','alarm_type','alarm_time','longitude','latitude')
        return Response(queryset.data)





# Create your views here.
