from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, UserProfile, UserVital




class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'email', 'password1', 'password2', 'national_id', 'phone')



# inherit from forms.Form not ModelForm so it desn't need a model
class Login_Form(forms.Form):
    username = forms.CharField(label='username', required=False)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
        
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            return {'username':username, 'password':password}
        raise forms.ValidationError("Invalid login")
            
      
            
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user','birth_date', 'sex')



class UserVitalForm(forms.ModelForm):
    class Meta:
        model = UserVital
        fields = '__all__'
        exclude = ('user',)
 
 