from django import forms
from django.forms import DateTimeInput
from django.forms import ModelForm
from datetime import datetime
from .models import Appointment
from django.utils import timezone
from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput
from django.utils import timezone, dateformat




#CONTACT FORM

class Contactform(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Name'}
    ))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Email'}
    ))
    content = forms.CharField(required= True, widget=forms.Textarea(
        attrs={"rows":5, "cols":20, 'class':'form-control','placeholder':'Message'}
    ))
    
    
#APPOINTMENT FORM

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'
    
class DateTimeForm(forms.Form):
    date= forms.DateField(widget= DateTimeInput())
   


class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeInput()
   
    
    

    class Meta:
        model = Appointment
        widgets = {'date': DateTimeInput()}
        fields = '__all__'
        
     #DATE VALIDATION
    def clean_date(self):
        date = self.cleaned_data.get('date','%Y-%m-%d')
        
        now= datetime.strftime(timezone.now(), '%Y-%m-%d')
     
        if str(date) > str(now):
            print(now)
            return date
        else:
            raise forms.ValidationError("The date is not available!")
      
        
    