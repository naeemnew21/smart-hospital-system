
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from rest_framework.permissions import BasePermission
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from user.models import MyUser
from user.serializers import StandardPagination
from rest_framework.response import Response
from datetime import date

from ys_appointment.models import AppointModel, RequsetAppointment
from ys_appointment.serializers import AppointSerializer, DrAppointSerializer

from ys_pharmacy.models import Medicine, Prescription, RequestPrescription
from ys_pharmacy.serializers import MedicineSerializer, PrescriptionSerializer



def doctor_check(user):
    if user.is_staff:
        try:
            return user.jobprofile.job == 'Dr'
        except:
            return False
    return False



class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            try:
                return request.user.jobprofile.job == 'Dr'
            except:
                return False
        return False
    
    
    

@user_passes_test(doctor_check, login_url='/login/' )
def dashboard(request):
    return render(request, 'doctor/dr.html')





    
    
class PatientsView(ListAPIView):
    serializer_class   = AppointSerializer
    pagination_class   = StandardPagination
    
    search_fields      = ['=patient__national_id', '=patient__phone', 'patient__email', 'patient__first_name']
    filter_backends    = (filters.SearchFilter,)
    
    permission_classes = [IsDoctor]
    
    def get_queryset(self):
        doctor   = self.request.user.id
        queryset = AppointModel.objects.filter(doctor = doctor, request_appointment__discharge = True)
        return queryset
    


    
      
class DrTodayAppointApi(ListAPIView):
    serializer_class   = DrAppointSerializer
    permission_classes = [IsDoctor]
    
    def get_queryset(self):
        doctor   = self.request.user.id
        queryset = AppointModel.objects.filter(doctor = doctor,
                                               appointment_date = date.today(),
                                               request_appointment__confirm   = True,
                                               request_appointment__discharge = False,
                                               request_appointment__reject    = False,
                                               request_appointment__disabled  = False
                                               )
        return queryset




  



class PrescriptionRetrieveApi(RetrieveAPIView):
    queryset = Prescription.objects.all()
    serializer_class   = PrescriptionSerializer
    lookup_field       = "patient"
    permission_classes = [IsDoctor]
    
    def get_queryset(self):
        doctor   = self.request.user
        queryset = Prescription.objects.filter(doctor  = doctor,
                                                date = date.today()
                                              )
        return queryset
    



class MedicineCreateApi(CreateAPIView):
    serializer_class   = MedicineSerializer
    permission_classes = [IsDoctor]
    
    def perform_create(self, serializer):
        x              = serializer.save()
        doctor         = self.request.user
        patient_id     = self.request.data['patient']
        appoint_req_id = self.request.data['appoint_request']
        req_instance   = RequsetAppointment.objects.get(id = appoint_req_id)
        patient        = MyUser.objects.get(id = patient_id)
        pre            = Prescription.objects.filter(doctor  = doctor,
                                                 patient = patient,
                                                 date = date.today()
                                                )
        if pre.exists():
            pre[0].medicines.add(x)
        else :
            pres = Prescription.objects.create(doctor  = doctor,
                                               patient = patient,
                                               appoint = req_instance,
                                               date    = date.today()
                                              )
            pres.medicines.add(x)




class MedicineDeleteApi(DestroyAPIView):
    queryset           = Medicine.objects.all()
    serializer_class   = MedicineSerializer
    permission_classes = [IsDoctor]
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        doctor   = request.user
        # problem (check if doctor has this medicine)
        # ***
        # ***
        # ***
        # ***
        # ***
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
