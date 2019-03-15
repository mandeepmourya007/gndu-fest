from django import forms
from .models import event


class eventform(forms.ModelForm):
    organiser_name= event.objects.all()
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Event Name '}),required = True,max_length=30)
    detail = forms.Textarea()
    event_organisers = forms.ChoiceField(choices=organiser_name,required = True)
    image = forms.ImageField(required=True)
    date = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class': 'datepicker'}))

    class Meta():
        ordering = ['date']
        model = event
        fields = ['name','detail','event_organisers','image','date']
