from django.db import models


class Therapist(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nombre")
    image = models.ImageField( upload_to="Images")
    terapia = models.CharField(max_length=200,verbose_name="Terapia")
    description = models.TextField(default="R")
    
    class Meta:
            verbose_name="Therapy"
            verbose_name_plural="Therapist"
        
    def __str__(self):
        return self.name
    
    
class Therapy(models.Model):
    name = models.CharField(max_length=255 , verbose_name = "Nombre")
    image = models.ImageField(verbose_name="Foto", blank=True, null=True, upload_to="Images")
    description = models.TextField()
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE,blank=True, null=True)
    duration = models.IntegerField (verbose_name="Duracion (Tiempo) ",blank=True, null=True)
    price = models.IntegerField(verbose_name="Precio",blank=True, null=True)
    
    class Meta:
            verbose_name="Terapia"
            verbose_name_plural="Terapias"
        
    def __str__(self):
        return str(self.name)
    

class Review(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=255)
    description = models.TextField()
    age = models.IntegerField()
    
    class Meta:
            verbose_name="Review"
            verbose_name_plural="Reviews"
        
    def __str__(self):
        return self.name
    


class Appointment(models.Model):
        # choices_time
        TIME_CHOICES =(
                ("8:00", "8:00"),
                ("9:00", "9:00"),
                ("10:00", "10:00"),
                ("11:00", "11:00"),
                ("12:00", "12:00"),
                ("13:00", "13:00"),
                ("14:00", "14:00"),
                ("15:00", "15:00"),
                ("16:00", "16:00"),
                ("17:00", "17:00"),
                ("18:00", "18:00"),
                ("19:00", "19:00"),
                ("20:00", "20:00"),
                
)
  
        name = models.CharField(max_length=255, verbose_name="Name")
        surname = models.CharField(max_length=255, verbose_name = "Surname")
        phone_number = models.CharField(max_length=255, verbose_name = "Phone number")
        email = models.EmailField()
        date = models.DateTimeField()
        time = models.CharField( verbose_name = "Time", max_length=255,  choices=TIME_CHOICES)
        therapy = models.ForeignKey( Therapy, on_delete = models.CASCADE)
        comments = models.TextField() 
        
        class Meta:
                verbose_name = "Appointment"
                verbose_name_plural = "Appointments"
                
        def __str__(self):
                return self.name + ' ' + self.surname
                