from django import forms
from .models import CustomUser, UserProfile

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic', 'location']
