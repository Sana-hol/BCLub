from django import forms
from . import models

class ConfigMember(forms.ModelForm):
    class Meta:
        model = models.Members
        fields = ['member_name']
        labels = {"member_name": ""}
