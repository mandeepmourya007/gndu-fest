from django import forms
from .models import event





class eventform(forms.ModelForm):
    organiser_name= event.objects.all()
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Event Name '}),required = True,max_length=30)
    detail = forms.Textarea()
  #  event_organisers = forms.ChoiceField(choices=organiser_name,required = True)
    image = forms.ImageField(required=True)
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
        # SelectDateWidget(attrs={

        #    # 'class': 'glyphicon glyphicon-calendar'
        #     })

        )

    class Meta():
        ordering = ['date']
        model = event
        fields = ['name','detail','image','date']
        
