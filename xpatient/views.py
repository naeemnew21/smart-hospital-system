from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import BasePermission
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, GenericAPIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import filters
from datetime import date
from user.forms import ImageForm, UserProfileForm, UserForm
from user.models import MyUser, UserProfile, UserVital
from user.serializers import StandardPagination
from xstaff.models import JobProfile
from xstaff.serializers import DoctorJobSerializer
from xstaff_doctor.models import Doctor
from xstaff_doctor.serializers import DoctorSerializer

from ys_appointment.models import AppointModel, RequsetAppointment
from ys_appointment.serializers import AppointSerializer
from ys_laboratory.models import LabModel
from ys_laboratory.serializers import LabSerializer
from ys_pharmacy.models import Prescription
from ys_pharmacy.serializers import PrescriptionSerializer


def get_age(BD):  #BD = DateField
    today = date.today()
    delta = today - BD
    yy    = delta.days//365
    mm    = (delta.days%365)//30
    #dd    = (delta.days%365)%30
    return yy,mm



class PatientDetail(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name="patient/patient.html"
    login_url  = reverse_lazy('user:login')

    def get_object(self, queryset=None):
        obj = UserProfile.objects.get(user = self.request.user)
        return obj
    
    def get_context_data(self, **kwargs):
        context             = super().get_context_data(**kwargs)
        context['user_age'] = get_age(self.get_object().birth_date)
        return context
    
    



class EditBasics(LoginRequiredMixin, UpdateView):
    model = MyUser
    form_class = UserForm
    template_name = 'patient/edit_basics.html'
    success_url = reverse_lazy('patient:dashboard')
    login_url = reverse_lazy('user:login')
    
    def get_object(self, queryset=None):
        return self.request.user
    



@login_required
def edit_profile(request):
    userprofile = UserProfile.objects.get(user = request.user)
    if request.POST:
        form1 = UserProfileForm(request.POST)
        form2 = ImageForm(request.FILES)
        if form1.is_valid():
            form1 = UserProfileForm(request.POST, instance = userprofile)
            form1.save()
            return redirect('patient:dashboard')
        if form2.is_valid():
            form2 = ImageForm(request.POST, request.FILES, instance = userprofile)
            form2.save()
            return redirect('patient:dashboard')
    return render(request, 'patient/edit_profile.html', {'userprofile':userprofile})



@login_required
def book(request):
    from xstaff_doctor.models import SPECIALS
    return render(request, 'patient/appointment.html', {'fields': SPECIALS})




class IsUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    
    
class DoctorsView(ListAPIView):
    serializer_class   = DoctorSerializer
    pagination_class   = StandardPagination
    
    permission_classes = [IsUser]
    
    def get_queryset(self):
        search = self.request.query_params.getlist('search')
        if search:
            queryset = Doctor.objects.filter(specialty__in=search)
        else:
            queryset = Doctor.objects.all()
        return queryset
 
    



class AppointApi(GenericAPIView):
    serializer_class   = AppointSerializer
    permission_classes = [IsUser]
    
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        pk      = request.data['pk']
        adate   = request.data['date']
        #check if date available for doctor or not here
        #--------------
        tdata   = {'patient':request.user.id, 'doctor':pk, 'appointment_date':adate}
        exist   = AppointModel.objects.filter(**tdata).exists()
        if not(exist):
            serializer = self.get_serializer(data = tdata)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({'redirect':'/patient/'})
    
    
    def delete(self, request, *args, **kwargs):
        pk       = request.data['pk']
        instance = AppointModel.objects.get(id=pk)
        if instance.patient ==  request.user:
            if instance.request_appointment.discharge:
                instance.request_appointment.disabled = True
                instance.request_appointment.save()
                return Response({'redirect':'/patient/'})    
            instance.delete()
        return Response({'redirect':'/patient/'})    


    def get_queryset(self):
        user  = self.request.user
        queryset = AppointModel.objects.filter(patient = user, request_appointment__disabled = False)
        return queryset
    
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    



      
class PrescriptionListApi(ListAPIView):
    serializer_class   = PrescriptionSerializer
    permission_classes = [IsUser]
    
    def get_queryset(self):
        patient   = self.request.user.id
        queryset = Prescription.objects.filter(
                                               patient  = patient,
                                               appoint__discharge = True
                                               )
        return queryset



class LabsListApi(ListAPIView):
    serializer_class   = LabSerializer
    permission_classes = [IsUser]
    
    def get_queryset(self):
        patient   = self.request.user.id
        queryset = LabModel.objects.filter(
                                               patient  = patient,
                                               appoint__discharge = True
                                               )
        return queryset

