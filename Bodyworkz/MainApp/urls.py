from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('contact/', views.contacto ,name ="contacto"),
    path('automatic/', views.automatic ,name="automatic"),
    path('our_therapist/', views.our_therapist,name="our_therapist"),
    path('therapies/', views.therapies,name="therapies"),
    path('reviews/', views.review,name="reviews"),
    path('appointment/', views.appointment,name="appointment"),
    path('appointment_done/', views.appointment_done,name="appointment_done"),
    path('article/<int:therapy_id>/', views.article, name = "article"),
     
]