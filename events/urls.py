from django.contrib import admin
from django.urls import path,include
from .import views
app_name="events"
urlpatterns = [

    path("",views.eventf,name="event"),
    path("enterevent<slug:number>",views.enterevent,name="enterevent"),
    path("eventreg",views.eventreg,name="eventreg"),
    path("p",views.p),
    ]
