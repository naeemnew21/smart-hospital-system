from django import forms
from .models import JobProfile, JobDays


JOBLIST = [
    ('HR', 'HR'),
    ('Dr', 'Dr'),
    ('Nurse', 'Nurse'),
    ('Ph', 'Ph'),
]

DEGREELIST = [
    ('PH', 'PH'),
    ('colleague', 'colleague'),
    ('Master', 'Master'),
    ('Graduated', 'Graduated'),
]




class JobProfileForm(forms.ModelForm):
    job  = forms.CharField(choices= JOBLIST, max_length=20, required=True)
    degree = forms.CharField(choices= DEGREELIST, max_length=20, required=True)
    class Meta:
        model = JobProfile
        fields = '__all__'
        exclude = ('user', 'like', 'dislike')



class JobDaysForm(forms.ModelForm):
    class Meta:
        model = JobDays
        fields = '__all__'
 
 