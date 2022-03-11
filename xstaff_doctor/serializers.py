from rest_framework import serializers
from xstaff.helptools import get_date
from .models import Doctor


        
        
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialty']
    
    def to_representation(self, instance):
        data                  = super().to_representation(instance)
        context               = {}
        context['name']       = instance.user.first_name
        context['pk']         = instance.user.id
        job_instance          = instance.user.jobprofile
        context['experience'] = job_instance.experience
        context['degree']     = job_instance.degree
        context['work_days']  = []
        for day in job_instance.work_days.all():
            ctx = {'day':day.day_name, 'start': str(day.start_time)[:-3], 'end':str(day.end_time)[:-3], 'date':get_date(day.day_name)}
            context['work_days'].append(ctx)
                  
        data.update(context)
        return data


