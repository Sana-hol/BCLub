from django import forms

from . import models 
from Books.models import Books 
from Members.models import Members
from django.forms import ModelChoiceField
from django.forms import HiddenInput, Select
from django.forms import ModelChoiceField
  
class CreateClub(forms.ModelForm): 
    class Meta: 
        model = models.Clubs
        fields = ['club_name']
        labels = {"club_name": "Nome do clube:"}
        
class SetBook(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(SetBook, self).__init__(*args, **kwargs)
        self.fields['current_book'].label_from_instance = lambda obj: "%s" % (obj.book_title)
    class Meta: 
        model = models.Clubs
        fields = ['current_book', 'current_progress']
        labels = {"current_book": "Livro atual:", "current_progress": "Progresso do livro:"}
    current_book = ModelChoiceField(
        queryset=Books.objects.all(),
        to_field_name='book_title',
        widget=forms.Select(attrs={'class': 'form-control'}),)
    
        
class CreateClubRelationsAddMembers(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(CreateClubRelationsAddMembers, self).__init__(*args, **kwargs)
        self.fields['member'].label_from_instance = lambda obj: "%s" % (obj.member_name)
    class Meta: 
        model = models.ClubStatus
        fields = ['member']
    member = ModelChoiceField(
        queryset=Members.objects.all(),
        to_field_name='member_name',
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

class CreateClubRelations(forms.ModelForm): 
    class Meta: 
        model = models.ClubStatus
        exclude = ('member','club','club_status')
            