import email
from . models import Therapist, Therapy, Review, Appointment, Index
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, View
from django.shortcuts import render,reverse , redirect
from .forms  import Contactform, AppointmentForm, Testimonialsform
from django.core.mail import EmailMessage
from django.views.generic.edit import CreateView, FormMixin
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django import forms
from Calendar.demo import create_event
import datetime as dt

#Index
def index(request):
    therapy = Therapy.objects.all()
    therapist = Therapist.objects.all()
    reviews = Review.objects.all()
    index = Index.objects.all()

    return render (request,'index.html', {'therapy': therapy, 'therapist': therapist, 'reviews':reviews,'index':index})

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
                "Bodyworkz Message : New Message Contact ",
                "From {} {}\n\n wrote :\n\n {}".format(name ,email,content),
                "bodyworkz.com", ["bodyworkz90@gmail.com"],
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


#Testimonials

class Testimonials(ListView, FormMixin):
    model = Review
    template_name = 'review.html'

    form_class = Testimonialsform
    fields = ['__all__']
    success_url = reverse_lazy('review')


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Testimonialsform()
        return context
    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        age = self.request.POST.get('age')
        description = self.request.POST.get('description')

        testimonials_form = Testimonialsform(data=request.POST)
        if testimonials_form.is_valid():
            mail = EmailMessage(
                "New Testimonial to BodyWorkz : New Testimonial ",
                "From {} \n {} \n {}  wrote :\n\n {}".format(name,email,age,description),
                "bodyworkz.com", ["bodyworkz90@gmail.com"],

                reply_to = [email]
                )
            mail.send()
            testimonials_form.save()

        return redirect(reverse("automatic"))


#Appointment

class CreateAppointment(ListView, FormMixin):
    model = Therapy

    template_name = 'appointment_form.html'
    form_class = AppointmentForm
    fiels = ['__all__']
    success_url = reverse_lazy('appointment_done')
    context_object_name = "therapy"


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AppointmentForm

        return context


    #Function to send email
    def post(self, request, *args, **kwargs):


        #Information
        name= self.request.POST.get('name')
        surname = self.request.POST.get('surname')
        email= self.request.POST.get('email')
        phone_number = self.request.POST.get('phone_number')
        date = self.request.POST.get('date')
        now= datetime.strftime(timezone.now(), '%Y-%m-%d')
        date_time = datetime.strptime(date,'%Y-%m-%d')
        date_1= date_time.date()
        time = self.request.POST.get('time')
        more_time = self.request.POST.get('more_time')

        price_more_time=0
        if more_time == "10' more please":
            price_more_time =25

        elif more_time =="20' more please":
            price_more_time =50
        elif more_time == "30' more please":
            price_more_time =100
        else:
            price_more_time == 0
        therapy = self.request.POST.get('therapy')
        query_therapy = Therapy.objects.get(pk=therapy)
        terapia= str(query_therapy.name)
        price = str(query_therapy.price)
        duration = str(query_therapy.duration)

        comments = self.request.POST.get('comments')
        appointmnet_form = AppointmentForm(data=request.POST)

        total_price = int(price) + int(price_more_time)

        #Validation Date
        if str(date) >= str(now):
            mail = EmailMessage(
                "Bodyworkz Massage : NEW APPOINTMENT ",
                "Hello!  {} {}\n\n Your booking confirmation for the date: {}  time: {}hs \n\n  Email  {}\n \n Phone number {} \n \n Therapy {} \n \n Therapy time {} minutes + {} additional\n \n Price $ {} DKK \n \n Comments :\n  {} \n \n \n \n Thanks for booking this appointment , we will contact you as soon as possible!   \n \n  BodyWorkz -  Adress: PRINSESSEGADE 4A , CHRISTIANSHAVN, COPENHAGEN" .format(name ,surname,date_1,time,email,phone_number,terapia,duration,more_time,total_price,comments),
                "bodyworkz.com", ["nachovidondo@gmail.com",email],
                reply_to = [email])
            mail.send()

            #Function to get the client in Google calendar

            #create_event(name,surname,date,time,phone_number,email,terapia,comments)

            #Its everthing ok ? save it.
            appointmnet_form.save()
        else:
            return redirect(reverse("appointment_fail"))


        return redirect(reverse("appointment_done"))



def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def appointment_fail(request):
    return render(request,'appointment_fail.html')