from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import  settings
from . import views
from .views import *

urlpatterns = [
    path('myapp/', views.Login_get),
    path('myapp/alarm/<imei>', views.Alarmdata_get),
    path('myapp/location/<imei>', views.Locdata_get),
    path('myapp/upload/',views.upload_video,name='upload'),
    path('videos/',display,name='videos'),
    path('myapp/command', views.Command_get.as_view()),
    path('myapp/command-response', views.Commandresponse_get.as_view()),
    path('myapp/filter-alarm/',views.fetch_alarmby_type)
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
