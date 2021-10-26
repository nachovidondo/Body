from django import forms
from django.forms import DateTimeInput
from django.forms import ModelForm

from .models import Appointment


from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput

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
    

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'
    
class DateTimeForm(forms.Form):
    date= forms.DateField(widget= DateTimeInput)
     

class AppointmentForm(forms.ModelForm):

    
    class Meta:
        model = Appointment
        widgets = {'date': DateTimeInput()}
        fields = '__all__'
""""
        def __init__(self, *args, **kwargs):
            fields = (
            forms.DateTimeField(),
            forms.DateTimeField())
            super().__init__(fields, *args, **kwargs)
            """
            