from django.db import models
from user.models import MyUser, OverwriteStorage
from y_service.models import ServiceRequest
from datetime import datetime

from ys_appointment.models import RequsetAppointment


REPORTS = [
    ('CBC','CBC'),
    ('CRP','CRP'),
    ('ALT','ALT'),

]



def lab_upload(instance, filename):
    fname, *exten = filename.split(".")
    newname       = str(datetime.now()).split('.')[0].replace(':','')
    return "lab/%s/%s.%s"%(instance.model.patient.id, newname, exten[-1])



class LabModel(models.Model):
    patient  = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='patient_lab')
    doctor   = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='doctor_lab')
    category = models.CharField(max_length=50, blank=False, null=False) 
    appoint  = models.ForeignKey(RequsetAppointment , on_delete=models.SET_NULL , blank=True, null=True )

    def __str__(self):
        return self.category


class RequestLab(ServiceRequest):
    model      = models.ForeignKey(LabModel, on_delete=models.CASCADE, related_name='request_lab')
    result     = models.FileField(upload_to=lab_upload, blank=True, null=True, storage = OverwriteStorage())
    
    patient    = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='lab_patient')
    doctor     = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='lab_doctor')
    staff_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='lab_staff')