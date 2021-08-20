from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

#creating an User_Register form using Django's inbuilt form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
#creating an User_Update form using Django's inbuilt form        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class  Meta:
        model = User
        fields = ['username','email']
#creating an Profile_Update form using Django's inbuilt form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']