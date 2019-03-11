from django.contrib import admin
from django.urls import path,include
from .import views
app_name="events"
urlpatterns = [

    path("",views.eventf,name="event"),
    path("enterevent<int:number>",views.enterevent,name="enterevent"),
    path("p",views.p),
    ]
