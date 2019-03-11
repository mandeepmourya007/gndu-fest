from django.shortcuts import render,redirect
from events.models import event
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from events.models import announcements
from django.conf import settings
from django.contrib.auth.models import User

def home(request):
    # events=event.objects.all()
    # print(events[0].image)
    # print(events)
    if request.method=="POST":
        print(request.POST)
        u=request.POST.get("username")
        p=request.POST.get("password")
        user=authenticate(request,username=u,password=p)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request, 'Welcome to TechFest '+ u )
            return redirect("home")
    return render(request,"home.html")


def about(request):
    return render(request,"about.html")
def privacy(request):
    return render(request,"privacy.html")
def placement(request):
    return render(request,"placement.html")
@login_required(redirect_field_name='')
def announcement(request):
    announce = announcements.objects.all()
    return render(request,"announcement.html",{"announce":announce})
def announce(request,id):
    a=id
    announce = announcements.objects.filter(id=a)
    return render(request,"announcement2.html",{"announce":announce})
def log_out(request):
    logout(request)
    return redirect('home')
