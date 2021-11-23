from . models import Therapist, Therapy, Review, Appointment
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render,reverse , redirect
from .forms  import Contactform, AppointmentForm
from django.core.mail import EmailMessage
from django.views.generic.edit import CreateView
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy


#Index
def index(request):
    therapy = Therapy.objects.all()
    therapist = Therapist.objects.all()
    reviews = Review.objects.all()

    return render (request,'index.html', {'therapy': therapy, 'therapist': therapist, 'reviews':reviews})

#Contact
def contacto(request):
    contact_form = Contactform()
    therapy = Therapy.objects.all()
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
            
    return render (request, 'contact.html', {'form':contact_form, 'therapy':therapy })

#Automatic message after contact us and book us
def automatic(request):
    therapy = Therapy.objects.all()
    return render (request, 'automatic.html',{'therapy':therapy}) 

def appointment_done(request):
    therapy = Therapy.objects.all()
    return render (request, 'appointment_done.html',{'therapy':therapy}) 

#Our Therapist
def our_therapist(request):
    therapy = Therapy.objects.all()
    therapist = Therapist.objects.all()
    return render(request,'our_therapist.html',{'therapist':therapist, 'therapy':therapy})

#Our Therapies
def therapies(request):
    therapies= Therapy.objects.all()
    therapy = Therapy.objects.all()
    return render(request,'therapies.html',{'therapies':therapies,'therapy':therapy})

#Individual Therapies
def article(request, therapy_id):
    articles = get_object_or_404(Therapy, pk = therapy_id)
    therapy = Therapy.objects.all()
    return render (request,'article.html',{'articles' : articles, 'therapy':therapy})

#Individual Therapist
def article_therapist(self,request, therapist_id):
    article_therapist = get_object_or_404(Therapist, pk = therapist_id)
    therapy = Therapy.objects.all()
    terapeuta = self.request.GET.get("lang")
    if terapeuta:
        therapy = therapy.filter(therapist_id = terapeuta)
            
    
    return render(request,'article_therapist.html',{'article_therapist' : article_therapist, 'therapy':therapy})




#Prueba terapeuta

class TerapeutaList(ListView):
    template_name = "article_therapist.html"
    model = Therapist
    context_object_name = "therapist"
    
    def get_queryset(self):
        qs = Therapist.objects.all()
        terapista= self.request.GET.get("lang")
        print(terapista)
        qs = qs.filter(id=terapista)
        return qs
    

#review
def review(request):
    reviews= Review.objects.all()
    therapy = Therapy.objects.all()
    return render(request,'review.html',{'reviews':reviews, 'therapy':therapy})


    
#Appointment


class CreateAppointment(CreateView):
    model = Appointment
    template_name = 'appointment_form.html'
    form_class = AppointmentForm
    fiels = ['__all__']
    success_url = reverse_lazy('appointment_done')
    #Function to send email
    def form_valid(self,form):
        name= self.request.POST.get('name')
        surname = self.request.POST.get('surname')
        email= self.request.POST.get('email')
        phone_number = self.request.POST.get('phone_number')
        date = self.request.POST.get('date')
        date_time = datetime.strptime(date,'%Y-%m-%d')
        date_1= date_time.date()
        time = self.request.POST.get('time')
        therapy = self.request.POST.get('therapy')
        query_therapy = Therapy.objects.get(pk=therapy)
        terapia= str(query_therapy.name)
        price = str(query_therapy.price)
        time = str(query_therapy.duration)
        comments = self.request.POST.get('comments')
        mail = EmailMessage(
                "Bodyworkz Massage : NEW APPOINTMENT ",
                "Hello!  {} {}\n\n Your booking confirmation for the date-time {} \n\n  Email  {}\n \n Phone number {} \n \n Therapy {} \n \n Therapy time {} minutes \n \n price $ {} DKK \n \n Comments :\n  {} \n \n \n \n Thanks for books us , we will contact you as soon as possible! \n \n BodyWorkz".format(name ,surname,date_1,email,phone_number,terapia,time ,price,comments),
                "bodyworkz.com", ["nachovidondo@gmail.com",email],
                reply_to = [email]
                )
        
        mail.send() 
                 
        
        
        return super().form_valid(form)


def terms_conditions(request):
    return render(request, 'terms_conditions.html')