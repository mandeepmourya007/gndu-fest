from django.contrib import admin
from django.urls import path,include
from .import views
app_name="events"
urlpatterns = [

    path("",views.eventf,name="event"),
    
    path("eventreg",views.eventreg,name="eventreg"),
    path("p",views.p),
    path("enterevent/<str:name>",views.enterevent,name="enterevent"),
    path("show_events_registered",views.show_events_registed,name="dashboard"),
    path("deatilevent/<str:name>",views.eventdetail,name="detailevent"),
    path("organiser/<str:email>",views.organiser_show,name="organiser"),
    path("studentp/<str:ename>",views.student_show,name="student"),


   # path("enterevent/<str:name>/<int:id>",views.ticket,name="ticket"),
    ]
