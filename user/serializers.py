from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from xstaff.models import JobProfile
from .models import MyUser


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'national_id', 'first_name', 'is_staff', 'is_active']
        read_only_fields = ['id', 'national_id', 'first_name']
        
    def to_representation(self, instance):
        data    = super().to_representation(instance)
        context = {}
        if instance.is_staff:
            #item    = JobProfile.objects.get(user = instance)
            item                  = instance.jobprofile
            context['job_id']     = item.id
            context['job']        = item.job
            context['experience'] = item.experience
            context['degree']     = item.degree
            context['work_days']  = []
            for day in item.work_days.all():
                ctx = {'day':day.day_name, 'start': day.start_time, 'end':day.end_time}
                context['work_days'].append(ctx)
            
            if item.job == 'Dr':
                doc              = instance.doctor
                context['dr_id'] = doc.id
                context['dr']    = doc.specialty
                
            if item.job == 'Secretary':
                Sec                = instance.secretary
                context['sec_id']  = Sec.id
                context['sec_doc'] = Sec.doctor
                if Sec.doctor :
                    context['sec_doc'] = Sec.doctor.user.national_id
                
        data.update(context)
        return data
        

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
        


