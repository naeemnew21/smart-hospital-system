from django.db import models
from user.models import MyUser, OverwriteStorage
from y_service.models import ServiceRequest
from datetime import datetime


XRAYS = [
    ('A','A'),
    ('B','B'),
    ('C','C'),
]



def xray_upload(instance, filename):
    fname, exten = filename.split(".")
    newname      = str(datetime.now()).split('.')[0].replace(':','')
    return "xray/%s/%s.%s"%(instance.model.patient.id, newname, exten)



class XRayModel(models.Model):
    patient = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='patient_xray')
    doctor  = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='doctor_xray')
    xray    = models.CharField(choices = XRAYS, max_length=50, blank=False, null=False) 

    def __str__(self):
        return self.xray


class RequsetXRay(ServiceRequest):
    model  = models.ForeignKey(XRayModel, on_delete=models.CASCADE, related_name= 'request_xray')
    result = models.FileField(upload_to=xray_upload, blank=True, null=True, storage = OverwriteStorage())
    
    patient    = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='xray_patient')
    doctor     = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='xray_doctor')
    staff_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='xray_staff')