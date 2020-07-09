from django.forms import ModelForm

from .models import *

class AddBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['user']
		