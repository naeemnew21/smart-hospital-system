from django.db import models
from user.models import MyUser
from y_service.models import ServiceRequest
from ys_appointment.models import RequsetAppointment


DISEASES = [
    ('cold','cold'),
    ('headech','headech'),
    ('painkiller','painkiller'),
]

UNITS = [
    ('Tab', 'Tab'),
    ('ml', 'ml')
]

TIMES = [
    ('After', 'After'),
    ('Before', 'Before')
]



class Pharmacy(models.Model):
    medicine_name = models.CharField( max_length=100, unique=True, blank=False, null=False)
    quantity      = models.IntegerField( default=0)
    price         = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    category      = models.CharField(choices = DISEASES, max_length=50, blank=True, null=True) 

    def __str__(self):
        return self.medicine_name  
    
    
    
    
class Medicine(models.Model):
    medicine_name   = models.CharField(max_length=100, blank=False, null=False)
    number_of_units = models.IntegerField() 
    unit            = models.CharField(choices = UNITS, max_length=50, blank=True, null=True) # optional
    number_of_times = models.PositiveIntegerField()
    time            = models.CharField(choices = TIMES, max_length=50, blank=True, null=True) # optional
    notes           = models.CharField(max_length=150, blank=True, null=True)  # optional
    #type --> Tab, drink, injection...
    
    def __str__(self):
        return self.medicine_name




class Prescription(models.Model):
    patient    = models.ForeignKey( MyUser , on_delete=models.SET_NULL , blank=True, null=True, related_name='patient_prescription')
    doctor     = models.ForeignKey( MyUser , on_delete=models.SET_NULL , blank=True, null=True, related_name='doctor_prescription')
    medicines  = models.ManyToManyField(Medicine, blank=True)
    date       = models.DateField(auto_now_add=True)
    appoint    = models.OneToOneField(RequsetAppointment , on_delete=models.SET_NULL , blank=True, null=True )
    
    def __str__(self):
        if self.patient and self.doctor:
            return self.doctor.first_name + ' -->> ' + self.patient.first_name
        return 'Unknown'



class RequestPrescription(ServiceRequest):
    model      = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='request_prescription')
    
    patient    = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='prescription_patient')
    doctor     = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='prescription_doctor')
    staff_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='prescription_staff')

