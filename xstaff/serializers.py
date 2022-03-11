from rest_framework import serializers
from .models import JobProfile, JobDays
from .helptools import get_date

class JobProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobProfile
        fields = ['job', 'experience', 'degree']
        


class JobDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDays
        fields = ['day_name', 'start_time', 'end_time']
        
            
    

class DoctorJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobProfile
        fields = ['experience', 'degree']
        
    
    def to_representation(self, instance):
        data                 = super().to_representation(instance)
        context              = {}
        context['name']      = instance.user.first_name
        context['pk']        = instance.user.id
        context['work_days'] = []
        for day in instance.work_days.all():
            ctx = {'day':day.day_name, 'start': str(day.start_time)[:-3], 'end':str(day.end_time)[:-3], 'date':get_date(day.day_name)}
            context['work_days'].append(ctx)
        
        if instance.job == 'Dr':
            doc                   = instance.user.doctor
            context['specialty']  = doc.specialty
                
        data.update(context)
        return data
        
