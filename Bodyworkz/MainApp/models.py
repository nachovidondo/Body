from django.db import models


class Therapist(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nombre")
    image = models.ImageField(upload_to="images")
    terapia = models.CharField(max_length=200,verbose_name="Terapia")
    description = models.TextField(default="R")
    
    class Meta:
            verbose_name="Therapy"
            verbose_name_plural="Therapist"
        
    def __str__(self):
        return self.name
    
    
class Therapy(models.Model):
    name = models.CharField(max_length=255 , verbose_name = "Nombre")
    image = models.ImageField(verbose_name="Foto", blank=True, null=True)
    description = models.TextField()
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE,blank=True, null=True)
    duration = models.IntegerField (verbose_name="Duracion (Tiempo) ",blank=True, null=True)
    price = models.IntegerField(verbose_name="Precio",blank=True, null=True)
    
    class Meta:
            verbose_name="Terapia"
            verbose_name_plural="Terapias"
        
    def __str__(self):
        return self.name
    

class Review(models.Model):
    name = models.CharField(verbose_name="nombre", max_length=255)
    description = models.TextField()
    age = models.IntegerField()
    
    class Meta:
            verbose_name="Review"
            verbose_name_plural="Reviews"
        
    def __str__(self):
        return self.name
    


class Offer(models.Model):
    expiration_date = models.DateField(null=True)