
from django.urls import path
from . import views

app_name = 'secretary'


urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('patients/', views.SecretaryAppointApi.as_view(), name = 'patients'),
    
]




