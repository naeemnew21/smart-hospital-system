from datetime import date, datetime
from rest_framework import serializers

from xstaff.models import JobDays
from .models import AppointModel, RequsetAppointment



def get_age(BD):  #BD = DateField
    today = date.today()
    delta = today - BD
    yy    = delta.days//365
    mm    = (delta.days%365)//30
    #dd    = (delta.days%365)%30
    return ''.join((str(yy),' years - ', str(mm), ' months'))




class AppointSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointModel
        fields = ['patient', 'doctor', 'appointment_date']
        
    def to_representation(self, instance):
        data                     = super().to_representation(instance)
        context                  = {}
         
        context['id']            = instance.id
        context['patient_name']  = instance.patient.first_name
        context['doctor_name']   = instance.doctor.first_name
        context['specialty']     = instance.doctor.doctor.specialty
         
        day_name                 = instance.appointment_date.strftime("%a")
        context['week_day']      = day_name
         
        set                      = JobDays.objects.filter(day_name = day_name, jobprofile__user = instance.doctor.id)
        context['start_time']    = str(set[0].start_time)[:-3]
        context['end_time']      = str(set[0].end_time)[:-3]
         
        context['status']        = instance.request_appointment.get_current()
        context['request_model'] = instance.request_appointment.id
        
        data.update(context)
        return data
        


class DrAppointSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointModel
        fields = ['patient']
        
    def to_representation(self, instance):
        data                       = super().to_representation(instance)
        context                    = {}
        context['appoint_id']      = instance.id
        context['appoint_request'] = instance.request_appointment.id
        patient                    = instance.patient
        context['patient_name']    = patient.first_name
        context['sex']             = patient.userprofile.sex
        context['marital_status']  = patient.userprofile.marital_status
        context['blood_type']      = patient.userprofile.blood_type
        context['age']             = get_age(patient.userprofile.birth_date)
        context['avatar']          = patient.userprofile.avatar.url
         
        
        data.update(context)
        return data      
        
 
class RequsetAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequsetAppointment
        fields = ['discharge', 'confirm', 'reject']
        

                               