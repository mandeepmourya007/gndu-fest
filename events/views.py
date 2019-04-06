from django.shortcuts import render,HttpResponse,redirect
from .models import event
from .forms import eventform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from accounts.models import studentsignup
from .models import student_registered_events
def eventf(request):
    events=event.objects.all()

    print(events)
    print(events)

    return render(request,"events/event.html",{"events":events})
def p(request):
    events=event.objects.all()
    return render(request,"events/p.html",{"events":events})

# def enterevent(request,number):

#     events = event.objects.filter(id = number)
#     return render(request,"events/enterevent.html",{ "events":events})

#@login_required
def enterevent(request,name):

    if(request.user.is_authenticated):
        email  = request.user
        print(email)
        print(email)
        print(email)
        payment = 'UNPAID'
        events = event.objects.filter(name = name)[0]
        #print("\n" +str(events))
        s = student_registered_events(email=email,event_name=events)
        ss=student_registered_events.objects.all()
        if(not s in ss):
           # s.save()
           print("\n data saved  ")
        else:
            print("\n data not saved  ")
            #return render(request,"events/ticket.html",{"data":"you are already registered for" + name+" event"})    
       # print(s.email)
      #  print(s.event_name)
        return render(request,"events/ticket.html",{"data":s.id})
    else:

        return redirect("accounts:login")

        
   # return render(request,"events/enterevent.html")

    

   




#@user_passes_test(lambda u: u.is_staff)
def eventreg(request):
    if request.method == 'POST':
        form = eventform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = eventform()
        emails=list(map(studentsignup.get_email,studentsignup.objects.all()))
        print(emails)
       # messages.success(request, 'your event registered successfully')

    return render(request, 'events/eventreg.html', {'form': form})
