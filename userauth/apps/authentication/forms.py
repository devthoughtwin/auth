from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from authentication.models import UserProfile

User = get_user_model()

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = ['first_name' ,'last_name' ,'mobile_number' , 'address', 'city' ,'state' , 'zip_code', 'profile_pic', 'company_name'
        ]