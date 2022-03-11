from statistics import mode
from django.db import models
from user.models import MyUser




JOBLIST = [
    ('None', 'None'),
    ('HR', 'HR'),
    ('Dr', 'Dr'),
    ('Nurse', 'Nurse'),
    ('pharmacist', 'pharmacist'),
    ('Secretary', 'Secretary'),
]

DEGREELIST = [
    ('None', 'None'),
    ('PH', 'PH'),
    ('colleague', 'colleague'),
    ('Master', 'Master'),
    ('Graduated', 'Graduated'),
]


DAYS = [
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
]



class JobDays(models.Model):
    day_name   = models.CharField(choices= DAYS, max_length=3, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time   = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.day_name
    
    def save(self, *args, **kwargs):
        exist = JobDays.objects.filter(day_name=self.day_name , start_time=self.start_time, end_time=self.end_time ).exists()
        if exist:
            return
        super().save(*args, **kwargs)


class JobProfile(models.Model):
    user       = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='jobprofile')
    job        = models.CharField(choices= JOBLIST, max_length=20, default="None")
    experience = models.IntegerField(default=0)
    degree     = models.CharField(choices= DEGREELIST, max_length=20, default="None")
    
    like      = models.IntegerField(default=0) # give like
    dislike   = models.IntegerField(default=0) # give dislike
    
    work_days  = models.ManyToManyField(JobDays, blank=True)
    
    def __str__(self):
        return self.user.national_id



    