from django import forms
from django.forms import DateTimeInput
from django.forms import ModelForm

from .models import Offer


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



from django.forms import ModelForm
from .models import Offer
 
class DateInput(forms.DateInput):
    input_type = 'date'
 
class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
        widgets = {
            'expiration_date': DateInput(),
            'time' : forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        }