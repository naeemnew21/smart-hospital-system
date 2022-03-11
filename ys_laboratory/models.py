from django.db import models
from user.models import MyUser, OverwriteStorage
from y_service.models import ServiceRequest
from datetime import datetime


REPORTS = [
    ('CBC','CBC'),
    ('CRP','CRP'),
    ('ALT','ALT'),

]



def lab_upload(instance, filename):
    fname, exten = filename.split(".")
    newname      = str(datetime.now()).split('.')[0].replace(':','')
    return "lab/%s/%s.%s"%(instance.model.patient.id, newname, exten)



class LabModel(models.Model):
    patient  = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='patient_lab')
    doctor   = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='doctor_lab')
    category = models.CharField(choices = REPORTS, max_length=50, blank=False, null=False) 

    def __str__(self):
        return self.category


class RequestLab(ServiceRequest):
    model  = models.ForeignKey(LabModel, on_delete=models.CASCADE, related_name='request_lab')
    result = models.FileField(upload_to=lab_upload, blank=True, null=True, storage = OverwriteStorage())
    