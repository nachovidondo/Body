from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('contact/', views.contacto ,name ="contacto"),
    path('automatic/', views.automatic ,name="automatic"),
    
]