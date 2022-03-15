from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework import filters
from django.db.models import Q
from itertools import chain 
from user.serializers import StandardPagination, UserSerializer
from xstaff.models import JobDays, JobProfile
from user.models import MyUser
from xstaff.serializers import JobDaysSerializer, JobProfileSerializer
from xstaff_doctor.models import SPECIALS, Doctor
from xstaff_doctor.serializers import DoctorSerializer
from xstaff.models import JOBLIST, DEGREELIST
from xstaff_secretary.models import Secretary
from xstaff_secretary.serializers import SecretarySerializer



def hr_check(user):
    if user.is_staff:
        try:
            return user.jobprofile.job == 'HR'
        except:
            return False
    return False



class IsHr(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            try:
                return request.user.jobprofile.job == 'HR'
            except:
                return False
        return False
    
    
    

@user_passes_test(hr_check, login_url='/login/' )
def dashboard(request):
    return render(request, 'hr/hr.html')



class UsersView(ListAPIView):
    serializer_class   = UserSerializer
    pagination_class   = StandardPagination
    
    search_fields      = ['=national_id', 'first_name', 'is_staff', 'jobprofile__job']
    filter_backends    = (filters.SearchFilter,)
    
    permission_classes = [IsHr]
    
    def get_queryset(self):
        query_patient      = MyUser.objects.filter(is_superuser=False, is_staff=False)
        query_staff        = MyUser.objects.filter(is_superuser=False, is_staff=True).exclude(jobprofile__job='HR')
        #queryset           = list(chain(query_patient,query_staff))
        queryset           = query_patient | query_staff
        return queryset
    

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        #print(response.data)
        response.data['degreelist'] = [i[0] for i in DEGREELIST]
        response.data['specials']   = [i[0] for i in SPECIALS]
        response.data['joblist']    = [i[0] for i in JOBLIST]
        return response
    
    



class UserUpdateView(UpdateAPIView):
    queryset           = MyUser.objects.all()
    serializer_class   = UserSerializer
    permission_classes = [IsHr]
    

class JobUpdateView(UpdateAPIView):
    queryset           = JobProfile.objects.all()
    serializer_class   = JobProfileSerializer
    permission_classes = [IsHr]
    
    def put(self, request, *args, **kwargs):
        obj        = self.get_object()
        job_before = obj.job
        response   = self.update(request, *args, **kwargs)
        obj        = self.get_object()
        job_after  = obj.job
        if job_after != job_before:
            if job_before == 'Dr':
                doctor = Doctor.objects.get(user = obj.user)
                doctor.delete()
            if job_before == 'Secretary':
                sec = Secretary.objects.get(user = obj.user)
                sec.delete()
        return response
    
    
    
class DrUpdateView(UpdateAPIView):
    queryset           = Doctor.objects.all()
    serializer_class   = DoctorSerializer
    permission_classes = [IsHr]
    


class SecretaryUpdateView(UpdateAPIView):
    queryset           = Secretary.objects.all()
    serializer_class   = SecretarySerializer
    permission_classes = [IsHr]
    
        
    def update(self, request, *args, **kwargs):
        nid = request.data['doctor']
        doctor = Doctor.objects.get(user__national_id = self.request.data['doctor'])
        instance = self.get_object()
        serializer = SecretarySerializer(instance = instance , data = {'doctor':doctor.id}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'doctor':nid}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AddDelDay(GenericAPIView):
    queryset           = JobDays.objects.all()
    serializer_class   = JobDaysSerializer
    permission_classes = [IsHr]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        
        exist = JobDays.objects.filter(**serializer.data).exists()
        if not(exist):
            self.create(request, *args, **kwargs)
            
        obj      = get_object_or_404(self.queryset, **serializer.data)
        instance = self.get_object()
        days     = instance.work_days.all()
        if obj in days:
            return JsonResponse({"detail":"already exists"})
        else:
            instance.work_days.add(obj)
        
        response = JobDaysSerializer(instance.work_days.all(), many=True)
        return Response(response.data)
    
    
    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        obj        = get_object_or_404(self.queryset, **serializer.data)
        instance   = self.get_object()
        days       = instance.work_days.all()
        if obj in days:
            instance.work_days.remove(obj)
        response = JobDaysSerializer(instance.work_days.all(), many=True)
        return Response(response.data)
    
    
    def get_object(self):
        queryset = JobProfile.objects.all()
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
   