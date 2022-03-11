
from django.urls import path
from . import views

app_name = 'patient'


urlpatterns = [
    path('', views.PatientDetail.as_view(), name = 'dashboard'),
    path('update/', views.EditBasics.as_view(), name = 'edit_basics'),
    path('appointments/', views.DoctorsView.as_view(), name = 'appointments'),
    
    path('myappoints/', views.AppointApi.as_view(), name = 'myappoints'),
    path('pres/', views.PrescriptionListApi.as_view(), name = 'prescriptions'),
    
    path('edit/', views.edit_profile, name = 'edit_profile'),
    path('book/', views.book, name = 'book'),
    
    
    
]





