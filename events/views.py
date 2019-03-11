from django.shortcuts import render
from .models import event
from django.contrib.auth.models import User


def eventf(request):
    events=event.objects.all()

    print(events)
    print(events)

    return render(request,"events/event.html",{"events":events})
def p(request):
    events=event.objects.all()
    return render(request,"events/p.html",{"events":events})

def enterevent(request,number):

    events = event.objects.filter(id = number)
    return render(request,"events/enterevent.html",{ "events":events})
