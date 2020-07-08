from django.forms import ModelForm

from .models import *

class UpdateDashboardForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']