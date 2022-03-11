from django.db import models
from user.models import MyUser
from xstaff_doctor.models import Doctor





class Secretary(models.Model):
    user   = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True, related_name="secretary")
    
    
    def __str__(self):
        return self.user.first_name

