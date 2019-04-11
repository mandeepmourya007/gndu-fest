from django import forms
from .models import studentsignup
from django.contrib.auth.models import User

class studentreg(forms.ModelForm):
    sem = (('I', 'I'),
           ('II', 'II'),
           ('III', 'III'),
           ('IV', 'IV'),
           ('V', 'V'),
           ('VI', 'VI'),
           ('VII', 'VII'),
           ('VIII', 'VIII'),

           )

    dept_name = (('BTECH-CSE', 'BTECH-CSE'),
                 ('BTECH-CIVIL', 'BTECH-CIVIL'),
                 ('BTECH-MECHANICAL', 'BTECH-MECHANICAL'),)
    roll_no = forms.CharField(widget = forms.TextInput(attrs={'class':'input-group ','placeholder':'Roll No'}),required = True,max_length=25)
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class':'input-group','placeholder':'First Name'}),required = True,max_length=60)
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class':'input-group','placeholder':'Last Name'}),required = True,max_length=60)

    department_name = forms.ChoiceField(choices=dept_name,required = True)

    semester = forms.ChoiceField(choices=sem,required = True)

    mobile_number = forms.CharField(widget = forms.TextInput(attrs={'class':'form-group input-group','placeholder':'Mobile No' }),required = True,max_length=10)
    email_id = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-group input-group','placeholder':'Email'}),required = True,max_length=40)
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-group input-group','placeholder':'Password'}),required = True,max_length=10)
   # password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-group input-group','placeholder':'confirm Password'}),required = True,max_length=100)

    class Meta():
        ordering = ['roll_no']
        model = studentsignup
        fields = ['roll_no','first_name','last_name','department_name','semester','mobile_number','email_id','password']



class userform(forms.ModelForm):

    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'First Name '}),required = True,max_length=30)
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Last Name'}),max_length = 30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}),required=True,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),required = True,max_length= 50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),required=True,max_length=50)

    class Meta():
        model = User
        fields = ['first_name','last_name','email','password']
