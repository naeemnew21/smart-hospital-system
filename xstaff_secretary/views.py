from datetime import date, datetime
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ys_appointment.models import AppointModel, RequsetAppointment
from ys_appointment.serializers import AppointSerializer, RequsetAppointmentSerializer




def secretary_check(user):
    if user.is_staff:
        try:
            return user.jobprofile.job == 'Secretary'
        except:
            return False
    return False



class IsSecretary(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            try:
                return request.user.jobprofile.job == 'Secretary'
            except:
                return False
        return False
    
    
    

@user_passes_test(secretary_check, login_url='/login/' )
def dashboard(request):
    return render(request, 'secretary/secretary.html')






class SecretaryAppointApi(GenericAPIView):
    serializer_class   = AppointSerializer
    permission_classes = [IsSecretary]
    
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        pk      = request.data['pk']
        event   = request.data['event']
        model   = RequsetAppointment.objects.get(id = pk)
        serializer = RequsetAppointmentSerializer(instance = model , data = {event: True}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        doctor   = self.request.user.secretary.doctor.user.id
        queryset = AppointModel.objects.filter(doctor = doctor, appointment_date = date.today(), request_appointment__disabled = False)
        return queryset
    
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
