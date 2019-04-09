from django.shortcuts import render,HttpResponse,redirect
from .models import event
from .forms import eventform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from accounts.models import studentsignup
from .models import student_registere_event
def eventf(request):
    if(request.user.is_authenticated):
        email = request.user
        events = event.objects.all()
        student_already = student_registere_event.objects.filter(email=email)
        print(student_already)
        return render(request,"events/event.html",{"events":events})
        

        
    else:
        events = event.objects.all()
        return render(request,"events/event.html",{"events":events})
        


def show_events_registed(request):
    email = request.user
    registed_events = student_registere_event.objects.filter(email=email)
    return render(request,"events/regevent.html",{"eventsp":registed_events})   
def p(request):
    #events=event.objects.all()
    ss=student_registere_event.objects.all()
    return render(request,"events/p.html",{"events":events})

# def enterevent(request,number):

#     events = event.objects.filter(id = number)
#     return render(request,"events/enterevent.html",{ "events":events})

#@login_required
def enterevent(request,name):

    if(request.user.is_authenticated):
        email  = request.user
        
       
        
        payment = 'UNPAID'
        events = event.objects.filter(name = name)[0]
        #print("\n" +str(events))
        s = student_registere_event(email=email,event_name=events)
        print(s,end="dd")
        #ss=student_registere_event.objects.filter(email=s['email'],event_name=s['event_name'])
        ss=student_registere_event.objects.filter(email=email,event_name=events)
        print(ss)

        if(ss.count() is 0):
           s.save()
           print("\n data saved  ")
        else:
            print("\n data not saved  ")
            #return render(request,"events/ticket.html",{"data":"you are already registered for" + name+" event"})    
       # print(s.email)
      #  print(s.event_name)
        return render(request,"events/ticket.html",{"data":s.id,"count":ss.count(),'id':ss[0].id})
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
