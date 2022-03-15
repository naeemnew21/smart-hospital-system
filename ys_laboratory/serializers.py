from datetime import date, datetime
from rest_framework import serializers

from xstaff.models import JobDays
from .models import LabModel, RequestLab





class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabModel
        fields = ['patient', 'doctor', 'category', 'appoint']
        
    def to_representation(self, instance):
        data                     = super().to_representation(instance)
        context                  = {}
         
        context['id']            = instance.id
        context['date']          = instance.appoint.create_date
        context['patient_name']  = instance.patient.first_name
        #context['patient_id']  = instance.patient.national_id
        context['doctor_name']   = instance.doctor.first_name
        #context['doctor_id']   = instance.doctor.national_id
        
        data.update(context)
        return data