
from django.contrib import admin

from .models import Therapist,Therapy, Review

# Register your models here.

admin.site.register(Therapist)
admin.site.register(Therapy)
admin.site.register(Review)