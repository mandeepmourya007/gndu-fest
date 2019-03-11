from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name= "accounts"
urlpatterns = [

    path("login/",views.log_in,name="login"),

    path("signup/",views.sign_up,name="signup"),
    path("logout",views.log_out,name="logout"),
    path("studentform",views.studentform,name = "studentform"),
    path("activate/<str:uidb64>/<str:token>",views.activate,name='activate'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),


]
