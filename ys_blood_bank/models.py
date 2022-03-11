from django.db import models
from user.models import MyUser
from y_service.models import ServiceRequest


BLOODTYPES=[
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('O+','O+'),
    ('O-','O-'),

]

class Bloodbank(models.Model):
    category    = models.CharField(choices=BLOODTYPES, max_length=3 )
    quantity    = models.PositiveIntegerField() # in bags
    expire_date = models.DateField()
    
    donor       = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='bloodbank')
    check       = models.BooleanField(default = True) # check if donor is right and good
    entity_name = None # the name of hospital ar unit that donor donates with blood
    place       = None # place of blood bank
    location    = None # location of bags in blood bank


    def __str__(self):
        return self.category  



class BloodModel(models.Model):
    patient  = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='patient_bloodbank')
    doctor   = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='doctor_bloodbank')
    category = models.CharField(choices=BLOODTYPES, max_length=3 )
    quantity = models.PositiveIntegerField() # in bags
    
    def __str__(self):
        return self.category  


class RequestBlood(ServiceRequest):
    model = models.ForeignKey(BloodModel, on_delete=models.CASCADE, related_name='request_blood')
    
    patient    = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='blood_patient')
    doctor     = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='blood_doctor')
    staff_user = models.ForeignKey(MyUser, on_delete=models.SET_NULL , blank=True, null=True, related_name='blood_staff')

