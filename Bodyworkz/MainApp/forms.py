
from django.forms import DateTimeInput
from .models import Appointment, Review, Time_Available
from django import forms
from django.forms.widgets import TextInput


from datetime import datetime ,timedelta, timezone



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
    i_have_read_and_accept_terms_conditions = forms.BooleanField()
 #Filter to show activities only from now to the future 
    def __init__(self, *args, **kargs):
         super().__init__(*args, **kargs)
         now = datetime.now(timezone.utc)
         self.fields['time_available'].queryset = Time_Available.objects.filter(date__gte=now).order_by('date')

    class Meta:
        model = Appointment
        widgets = {'date': DateTimeInput()}
        fields = ['name','surname','phone_number','email','time_available','therapy','more_time','comments',]

#Testimonials FORM

class Testimonialsform(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Name'}
    ))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Email'}
    ))
    age = forms.CharField(required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Age'}
    ))

    description = forms.CharField(required= True, widget=forms.Textarea(
        attrs={"rows":5, "cols":20, 'class':'form-control','placeholder':'Testimonial'}
    ))

    class  Meta:
        model = Review
        fields = '__all__'