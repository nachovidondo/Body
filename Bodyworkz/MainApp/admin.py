
from django.contrib import admin
from . import models
from .models import Appointment, Therapist,Therapy, Review, Index, AboutUs, Time_Available

# Register your models here.

admin.site.register(Therapist)
admin.site.register(Therapy)
admin.site.register(Review)
admin.site.register(Appointment)
admin.site.register(Index)
admin.site.register(AboutUs)
@admin.register(models.Time_Available)
class Time_AvailableAdmin(admin.ModelAdmin):
    ordering = ['-date']