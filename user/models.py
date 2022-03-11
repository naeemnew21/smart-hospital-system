from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
import os
from project import settings
from django.utils.translation import gettext_lazy as _
from .validme import ID_Valid



BLOOD = [
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('O+','O+'),
    ('O-','O-'),
    ]

SOCIAL =[
    ('single','single'),
    ('married','married'),
    ('divorced','divorced')
    ]


SEX =[
    ('Male','Male'),
    ('Female','Female'),
    ('Unknown','Unknown')
    ]



def validate_id(value):
    if ID_Valid(value).is_valid() == False:
         raise ValidationError(
            _('%(value)s is not valid id'),
            params={'value': value},
        )
  
def validate_name(name):
    if not(name) or name.isspace():
         raise ValidationError(_('empty name is not valid name'))   


def image_upload(instance, filename):
    imgname, exten = filename.split(".")
    return "profile/%s.%s"%(instance.user.id, exten)



class OverwriteStorage(FileSystemStorage):
    
    def get_available_name(self, name, max_length = None):
        """
        def save(self, *args, **kwargs):
            try:
                this = MyModelName.objects.get(id=self.id)
                if this.MyImageFieldName != self.MyImageFieldName:
                    this.MyImageFieldName.delete()
            except: pass
            super(MyModelName, self).save(*args, **kwargs)
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
    
    



class MyUser(AbstractUser):
    email       = models.EmailField(verbose_name="email address", unique=True, blank=False, null=False)
    #user_type --> patient/employeee  --replaced with is_staff
    phone_regex = RegexValidator(regex="[0][1][0125][0-9][ ]?\d{3}[ ]?\d{4}", message="Phone number must be entered in the format: '01xx xxx xxxx'. Up to 11 digits allowed.")
    phone       = models.CharField(validators=[phone_regex], max_length=11, unique=True, blank=False, null=False) # validators should be a list
    national_id = models.CharField(max_length=14 , validators=[validate_id] , unique=True, blank=False, null=False)
    
    first_name  = models.CharField(verbose_name="first name", validators=[validate_name], max_length=30, blank=False, null=False)
    last_name   = models.CharField(verbose_name="last name", max_length=30, blank=True, null=True)
    
    REQUIRED_FIELDS = ['email', 'phone', 'national_id', 'first_name']

    def __str__(self):
        return self.national_id




class UserProfile(models.Model):
    user            = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    birth_date      = models.DateField()
    sex             = models.CharField(choices= SEX , max_length= 7)
    
    avatar          = models.ImageField(upload_to=image_upload, default = 'profile/avatar.png', storage = OverwriteStorage() )
    
    weight          = models.DecimalField(max_digits=6, decimal_places=3, default = 0) # in KG   
    height          = models.DecimalField(max_digits=4, decimal_places=1, default = 0) # in CM
    marital_status  = models.CharField(choices=SOCIAL , max_length= 8, blank=True, null=True)
    blood_type      = models.CharField(choices=BLOOD, max_length= 3, blank=True, null=True)
    
    def __str__(self):
        return self.user.national_id
    



class UserVital(models.Model):
    user                = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    heart_rate          = models.IntegerField(default = 0) # in bpm
    blood_pressure_up   = models.IntegerField(default = 0)
    blood_pressure_down = models.IntegerField(default = 0)
    respiration_rate    = models.IntegerField(default = 0)
    temprature          = models.DecimalField(max_digits=3, decimal_places=1, default = 0)
    
    def __str__(self):
        return self.user.national_id
    
