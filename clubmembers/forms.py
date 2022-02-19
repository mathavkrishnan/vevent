from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import events
class eventsform(ModelForm):
    class Meta:
        model = events
        fields = ['eventname','link','lastdate','eventdate','time','location','slots','poster']

