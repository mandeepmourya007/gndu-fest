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
        pass
    else:

        return redirect("accounts:login")

        
    return render(request,"events/enterevent.html")

    
def save(request,name):

    email  = str(request.user)
    print(email)
    print(email)
    print(email)
    payment = 'UNPAID'
    events = event.objects.filter(name = name)

    s = student_registered_events(email,events,payment)
    #s.save()
    return HttpResponse("registeration successfulll")

   




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
