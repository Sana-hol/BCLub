from django import forms 
from . import models 
from Members.models import Members
from django.forms import ModelChoiceField
from django.forms import HiddenInput, Select
from django.forms import ModelChoiceField

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.member_name  
        
class CreateClub(forms.ModelForm): 
    class Meta: 
        model = models.Clubs
        fields = ['club_name']
        labels = {"club_name": "Nome do clube:"}
        

        
class CreateClubRelationsAddMembers(forms.ModelForm): 
    class Meta: 
        model = models.ClubStatus
        fields = ['member']
    member = MyModelChoiceField(
        queryset=Members.objects.all(),
        to_field_name='member_name',
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

class CreateClubRelations(forms.ModelForm): 
    class Meta: 
        model = models.ClubStatus
        exclude = ('member','club','club_status')
            