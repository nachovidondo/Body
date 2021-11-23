
from django.contrib import admin

from .models import Appointment, Therapist,Therapy, Review

# Register your models here.

admin.site.register(Therapist)
admin.site.register(Therapy)
admin.site.register(Review)
admin.site.register(Appointment)