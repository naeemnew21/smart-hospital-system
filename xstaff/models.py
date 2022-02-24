from statistics import mode
from django.db import models
from user.models import MyUser




JOBLIST = [
    ('None', 'None'),
    ('HR', 'HR'),
    ('Dr', 'Dr'),
    ('Nurse', 'Nurse'),
    ('Ph', 'Ph'),
]

DEGREELIST = [
    ('None', 'None'),
    ('PH', 'PH'),
    ('colleague', 'colleague'),
    ('Master', 'Master'),
    ('Graduated', 'Graduated'),
]


class JobProfile(models.Model):
    user       = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    job        = models.CharField(choices= JOBLIST, max_length=20, default="None")
    expeience  = models.IntegerField(default=0)
    degree     = models.CharField(choices= DEGREELIST, max_length=20, default="None")
    
    like      = models.IntegerField(default=0) # give like
    dislike   = models.IntegerField(default=0) # give dislike
    
    start_time = models.TimeField(default = '00:00:00')
    end_time   = models.TimeField(default = '00:00:00')
    days       = models.ForeignKey('JobDays', on_delete=models.SET_NULL , null=True)
    
    def __str__(self):
        return self.user
    
    

class JobDays(models.Model):
    sat = models.BooleanField(default = False)
    sun = models.BooleanField(default = False)
    mon = models.BooleanField(default = False)
    tue = models.BooleanField(default = False)
    wed = models.BooleanField(default = False)
    thu = models.BooleanField(default = False)
    fri = models.BooleanField(default = False)
    