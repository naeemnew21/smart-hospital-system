from django.db import models
from user.models import MyUser



SPECIALS = [
    ('General','General'),
    ('Internist','Internist'),
    ('cardiologist','cardiologist'),
    ('Endocrinologist','Endocrinologist'),
    ('Hematologist ','Hematologist '),
    ('Nephrologist','Nephrologist'),
    ('Oncologist','Oncologist'),
    ('Rheumatologist ','Rheumatologist '),
    ('Surgeon','Surgeon'),
    ('Pediatrician ','Pediatrician '),
    ('Gynaecologist','Gynaecologist'),
    ('Ophthalmologist ','Ophthalmologist '),
    ('Neurologist','Neurologist'),
    ('ENT','ENT'),
    ('Urologist','Urologist'),
    ('Dermatologist','Dermatologist'),
    ('Hepatologist ','Hepatologist '),
    ('Psychologist','Psychologist'),
    ('Anesthesiologist','Anesthesiologist'),
    ('bones_doctor','bones_doctor'),
    ('Dentist','Dentist'),
    ('Anatomist','Anatomist')
    
]


class Doctor(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    specialty  = models.CharField(choices = SPECIALS, max_length=20, default='General')
    
    def __str__(self):
        return self.user.first_name
