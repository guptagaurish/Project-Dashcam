# Project-Dashcam
Stacks Used  - Django rest framework, Django, Python, HTML
imei is primary key for login and foreign key for rest functions.
for code files move url to https://github.com/guptagaurish/Project-Dashcam/tree/master

Assumption - 
command response will be send by Dashcam to Backend.
Videos are uploaded.


These are all urls to test - 

path('myapp/', views.Login_get),
    path('myapp/<imei>', views.Alarmdata_get),
    path('myapp/Location/<imei>', views.Locdata_get),
    path('myapp/upload/',views.upload_video,name='upload'),
    path('videos/',display,name='videos'),
    path('myapp/command', views.Command_get.as_view()),
    path('myapp/command-response', views.Commandresponse_get.as_view()),
  
