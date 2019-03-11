from django.db import models
from events.models import event
class student(models.Model):
    event=models.ManyToManyField(event)
    username=models.CharField( max_length=30,)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    def __str__(self):
        return self.username

class studentsignup(models.Model):
    dept_name = (('Dept_1', 'BTECH-CSE'),
                 ('Dept_2', 'BTECH-CIVIL'),
                 ('Dept_3', 'BTECH-MECHANICAL'),)

    sem = (('I', 'I'),
           ('II', 'II'),
           ('III', 'III'),
           ('IV', 'IV'),
           ('V', 'V'),
           ('VI', 'VI'),
           ('VII', 'VII'),
           ('VIII', 'VIII'),

           )
    roll_no = models.CharField(max_length=25,unique=True)
    name = models.CharField(max_length = 60)
    department_name = models.CharField(max_length=70, choices=dept_name,
                                       default='Dept_1')
    semester = models.CharField(max_length=10,
                                choices = sem, default='I')
    mobile_number = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=20)
    password = models.CharField(max_length = 100)

    class Meta():
        ordering = ['roll_no']
