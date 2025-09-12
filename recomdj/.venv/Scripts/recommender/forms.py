from django import forms
from .models import UserInterests, user

class NewUserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        

class UserInterestsForm(forms.ModelForm):
    class Meta:
        model = UserInterests
        fields = '__all__'