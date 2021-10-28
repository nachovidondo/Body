from . models import Therapist, Therapy, Review, Appointment
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render,reverse , redirect
from .forms  import Contactform, AppointmentForm
from django.core.mail import EmailMessage
from django.views.generic.edit import CreateView
from datetime import datetime


#Index
def index(request):
    therapy = Therapy.objects.all()
    therapist = Therapist.objects.all()
    reviews = Review.objects.all()

    return render (request,'index.html', {'therapy': therapy, 'therapist': therapist, 'reviews':reviews})

#Contact

def contacto(request):
    contact_form = Contactform()
    if request.method == "POST":  
        contact_form = Contactform(data=request.POST)
        if contact_form.is_valid(): 
            name= request.POST.get('name')
            email= request.POST.get('email')
            content= request.POST.get('content')
            mail = EmailMessage(
                "Bodyworkz Massage : Nuevo Mensaje de Contacto ",
                "De {} {}\n\nEscribio:\n\n {}".format(name ,email,content),
                "bodyworkz.com", ["nachovidondo@gmail.com"],
                reply_to = [email]
                )
            try:
                mail.send() #Si esta todo ok redireccionar
                return redirect(reverse("automatic")+"?ok")
                 
                 
            
            except:
                return redirect(reverse("contacto")+"?fail")
            
    return render (request, 'contact.html', {'form':contact_form })

#Automatic message after contact us
def automatic(request):
    return render (request, 'automatic.html') 

#Our Therapist
def our_therapist(request):
    therapist = Therapist.objects.all()
    return render(request,'our_therapist.html',{'therapist':therapist})

#Our Therapies
def therapies(request):
    therapies= Therapy.objects.all()
    return render(request,'therapies.html',{'therapies':therapies})


#review
def review(request):
    reviews= Review.objects.all()
    return render(request,'review.html',{'reviews':reviews})


    
#Appointment

def appointment(request):
    appointment_form = AppointmentForm()
    if request.method == "POST":  
        appointment_form = AppointmentForm(data=request.POST)
        if appointment_form.is_valid(): 
            name= request.POST.get('name')
            surname = request.POST.get('surname')
            email= request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            date = request.POST.get('date')
            date_time = datetime.strptime(date,'%Y-%m-%d')
            date_1= date_time.date()
            time = request.POST.get('time')
            therapy = request.POST.get('therapy')
          
            query_therapy = Therapy.objects.get(pk=therapy)
            terapia= str(query_therapy.name)
            price = str(query_therapy.price)
            time = str(query_therapy.duration)
            
            comments = request.POST.get('comments')
            
        
            
            mail = EmailMessage(
                "Bodyworkz Massage : NEW APPOINTMENT ",
                "Hello!  {} {}\n\n Your booking confirmation for the date-time {} \n\n  Email  {}\n \n Phone number {} \n \n Therapy {} \n \n Therapy time {} minutes \n \n price $ {} Dkk \n \n Comments :\n  {} \n \n \n \n Thanks for books us , we will contact you as soon as possible! \n \n BodyWorkz".format(name ,surname,date_1,email,phone_number,terapia,time ,price,comments),
                "bodyworkz.com", ["nachovidondo@gmail.com","email"],
                reply_to = [email]
                )
            try:
                mail.send() #Si esta todo ok redireccionar
                return redirect(reverse("automatic")+"?ok")
                 
                 
            
            except:
                return redirect(reverse("contacto")+"?fail")
            
    return render (request, 'appointment_form.html', {'form':appointment_form })