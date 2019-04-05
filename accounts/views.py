
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import student
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import studentreg, userform
from .models import studentsignup
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail


def log_out(request):
    logout(request)
    return redirect(('home'))
def log_in(request):

        if request.method=="POST":
            print(request.POST)
            u=request.POST.get("username")
            p=request.POST.get("password")
            user=authenticate(request,username=u,password=p)
           # print("\n" +user +"\n")
            if user is not None:
                login(request,user)
                messages.success(request, ' Welcome to Tech Fest '+ u )
                return redirect("home")
        return render(request,'accounts/login.html')


"""def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            s=student(username=username,password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})"""

def studentform(request):

    if request.method == 'POST':
        #print(request.POST)
        #print(request.POST.get("password2"))
        form = studentreg(request.POST)
            # name=request.POST.get('name'),
            # department_name=request.POST.get("department_name"),
            # roll_no=request.POST.get("roll_no"),
            # semester=request.POST.get("semester"),
            # email_id=request.POST.get("email_id"),
            # mobile_number=request.POST.get("mobile_number"),
            # password=request.POST.get("password2")



        if form.is_valid():
            form.save()
            username = form.cleaned_data['email_id']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email_id']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, first_name=first_name,
                                             last_name=last_name, email=email,
                                               password=password, is_active=False)
            current_site = get_current_site(request)
            uid3 = User.objects.get(pk=user.pk)
            # encod = user.email.encode('base64','strict'),
            userdetail = {'user': username,
                          'domain': current_site.domain,
                          # 'encod':encod,
                          'uid2': User.objects.get(pk=user.pk),

                          'uid': urlsafe_base64_encode(force_bytes(uid3)),

                          'token': account_activation_token.make_token(user)}
            message = "hii " + userdetail['user'] + "\nclick on link " + userdetail[
                'domain'] + "/accounts/activate" + "/" + str(userdetail['uid2']) + "/" + str(userdetail['token'])
            mail_subject = 'Activate your account.'
            to_email = form.cleaned_data.get('email_id')
            #email = EmailMessage(mail_subject, message, to=[to_email])
            #email.send()
            send_mail(
    mail_subject,
    message,
    ['noreply@Techfest.com'],
    [to_email],
)
            messages.success(request,'GO to your spam mail to activate your email ')
            return HttpResponse('Please confirm your email address to complete the registration')
      #  else:

      #      return HttpResponse('something went wrong Please try again')

    else:
        form = studentreg()

    return render(request,'accounts/studentform.html',{'form':form})


def sign_up(request):
    if request.method == 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['email']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password=form1.cleaned_data['password']
            user= User.objects.create_user(username=username,first_name=first_name,last_name =last_name,email=email,password =password,is_active=False)
            current_site = get_current_site(request)
            uid3 =User.objects.get(pk=user.pk),P[9]
            #encod = user.email.encode('base64','strict'),
            userdetail = {'user': username,
                'domain': current_site.domain,
                #'encod':encod,
                'uid2':User.objects.get(pk=user.pk),

                'uid': urlsafe_base64_encode(force_bytes(uid3)),

                'token': account_activation_token.make_token(user)}
            message = "hii "+ userdetail['user']+"\nclick on link "+userdetail['domain']+"/accounts/activate"+"/"+str(userdetail['uid2'])+"/"+str(userdetail['token'])
            mail_subject = 'Activate Your account.'
            to_email = form1.cleaned_data.get('email')
            #email = EmailMessage(mail_subject, message, to=[to_email])
            #email.send()
            send_mail(
    mail_subject,
    message,
    'noreply@Tech.com',
    [to_email],
)
            return HttpResponse('Please confirm your email address to complete the registration')
        else:

            return HttpResponseRedirect('somthing went wrong Pleasetry again')

    else:
        form1 = userform()
    return render(request,'accounts/register.html',{'form':form1})


def activate(request, uidb64, token):
    try:

        #uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(username=uidb64)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        u=user.first_name
        # return redirect('home')
        messages.success(request, ' link activated ' + u)
        return redirect("home")
    else:
        return HttpResponse('Activation link is invalid!')