from django import forms
from .models import Bloodbank, RequestBlood



class AddBloodForm(forms.ModelForm):
    class Meta:
        model = Bloodbank
        fields = ('category', 'quantity', 'expire_date', 'donor')
    
    def valid_date(self):
        # validate in models
        pass
 