from django.db import models
from user.models import MyUser
from y_service.models import ServiceRequest





class AppointModel(models.Model):
    patient          = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='patient_appointment')
    doctor           = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='doctor_appointment')
    appointment_date = models.DateField()

    def __str__(self):
        return str(self.appointment_date)


class RequsetAppointment(ServiceRequest):
    model      = models.OneToOneField(AppointModel, on_delete=models.CASCADE, related_name= 'request_appointment')
    
    patient    = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='appoint_patient')
    doctor     = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='appoint_doctor')
    staff_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='appoint_staff')


    def get_current(self):
        if self.reject:
            return 'rejected'
        if self.discharge:
            return 'discharged'
        if self.confirm:
            return 'accepted'
        return 'pending'