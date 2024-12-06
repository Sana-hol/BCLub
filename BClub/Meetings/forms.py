from django import forms

from . import models 
from Books.models import Books 
from Members.models import Members
from django.forms import ModelChoiceField
from django.forms import HiddenInput, Select
from django.forms import ModelChoiceField
  

class CreateMeeting(forms.ModelForm): 
    class Meta: 
        model = models.Meetings
        fields = ['meeting_name', 'meeting_local', 'meeting_date']
        labels = {'meeting_name:':'Titulo da reunião:', 'meeting_local':'Local da reunião:', 'meeting_date':'Data da reunião:'}
        