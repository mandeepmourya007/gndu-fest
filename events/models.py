from django.db import models
import datetime
from django.contrib.auth.models import User


class event_organisers(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class event(models.Model):
    name = models.CharField(max_length=100)
    detail=models.TextField()

    event_organisers = models.ManyToManyField('event_organisers',blank=True)

    image=models.FileField(null=True,blank=True,upload_to="static/events/images")
    price = models.CharField(max_length=10,default = 'Free')
    
    date_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.name




class announcements(models.Model):
    I = 'I'
    II='II'
    III='III'
    IV = 'IV'
    V =  'V'
    VI = 'VI'
    VII = 'VII'
    VIII = 'VIII'
    To_all = 'I-VIII'

    Dept_1='BTECH-CSE'
    Dept_2='BTECH-CIVIL'
    Dept_3='BTECH-MECHANICAL'
    sem = ((I, 'I'),
        (II, 'II'),
        (III, 'III'),
        (IV, 'IV'),
        (V, 'V'),
        (VI, 'VI'),
        (VII, 'VII'),
        (VIII, 'VIII'),
        (To_all,'I-VIII'),
           )
    dept_name = ((Dept_1,'BTECH-CSE'),
                 (Dept_2,'BTECH-CIVIL'),
                 (Dept_3,'BTECH-MECHANICAL'),)

    name =  models.CharField(max_length=100)
    detail=models.TextField()
    image=models.FileField(null=True,blank=True,upload_to="static/events/images")
    image_link = models.CharField(max_length=300, null=True, blank=True)
    department_name = models.CharField(max_length=70, choices=dept_name,
        default=Dept_1)
    semester = models.CharField(max_length=10,
        choices=sem,
        default=I,)
    name_of_announcer = models.CharField(max_length=50,)
    date_of_announcement = models.DateTimeField(auto_now = False)
    def __str__(self):
        return self.name


from django.contrib import admin

admin.site.register(announcements)
admin.site.register(event_organisers)


class student_registered_events(models.Model):
    pay_status = (('PAID','PAID'),
                 ('UNPAID','UNPAID'))
    email = models.ForeignKey(User,on_delete=models.CASCADE)
    event_name = models.ManyToManyField('event')
    payment = models.CharField(max_length=10, choices=pay_status,
        default='UNPAID')
    date_time = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return str(self.email)

from django.contrib import admin


admin.site.register(student_registered_events)
