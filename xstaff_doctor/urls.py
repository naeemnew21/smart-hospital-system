from django.urls import path
from . import views

app_name = 'doctor'


urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    
    path('patients/', views.PatientsView.as_view(), name = 'listpatient'),
    path('today/', views.DrTodayAppointApi.as_view(), name = 'listtoday'),
    
    #path('allpres/', views.AllPrescriptionsRetrieveApi.as_view(), name = 'allprescriptions'),
    path('pre/<int:patient>', views.PrescriptionRetrieveApi.as_view(), name = 'prescription'),
    path('addmed/', views.MedicineCreateApi.as_view(), name = 'addmedicine'),
    path('delmed/<int:pk>', views.MedicineDeleteApi.as_view(), name = 'delmedicine'),
    
    path('lab/<int:patient>', views.AnalysisListApi.as_view(), name = 'analysis'),
    path('addlab/', views.AnalysisCreateApi.as_view(), name = 'createlab'),
    path('dellab/<int:pk>', views.AnalysisDeleteApi.as_view(), name = 'deletelab'),

]

