from . models import Therapist, Therapy, Review
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render,reverse , redirect
from .forms  import Contactform
from django.core.mail import EmailMessage


#Index
def index(request):
    therapy = Therapy.objects.all()

    return render (request,'index.html', {'therapy': therapy})

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
                "bodyworkz.com", ["ignaciovidondo@hotmail.com"],
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