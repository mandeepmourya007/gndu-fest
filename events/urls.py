from django.contrib import admin
from django.urls import path,include
from .import views
app_name="events"
urlpatterns = [

    path("",views.eventf,name="event"),
    
    path("eventreg",views.eventreg,name="eventreg"),
    path("p",views.p),
    path("enterevent/<slug:name>",views.enterevent,name="enterevent"),
    #path("enterevent/<slug:name>",views.save,name="enterevent"),
    ]
