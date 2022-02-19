from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import regevents
class regform(ModelForm):
    class Meta:
        model = regevents
        fields = ['user','eventname','link','eventdate','time','location']