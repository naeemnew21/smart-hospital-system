from django import forms
from .models import RequsetAppointment





 
class CreateAppointForm(forms.ModelForm):
    class Meta:
        model = RequsetAppointment
        fields = ('appointment_date',)
    
    def valid_date(self):
        pass
 
 
 
 
class StaffAppointForm(forms.ModelForm):
    class Meta:
        model = RequsetAppointment
        fields = ('confirm',)
        
        

class RejectAppointForm(forms.ModelForm):
    class Meta:
        model = RequsetAppointment
        

class CancelAppointForm(forms.ModelForm):
    class Meta:
        model = RequsetAppointment
