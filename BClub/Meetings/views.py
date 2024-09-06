import time
from django.contrib import messages
from django.db.models import F
from django.shortcuts import render, redirect
from Books.models import Books
from Members.models import Members
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ClubStatus, Clubs
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
@login_required(login_url = '/Members/login')
def meeting_new (request, club_id): 
    if request.method == 'POST': 
        form = forms.CreateMeeting(request.POST) 
        if form.is_valid():
            newclub = form.save(commit=False)
            newclub.club = club_id
            newclub.save()
            if form2.is_valid():
                newrelation = form2.save(commit=False)
                newrelation.member = Members.objects.get(account=request.user)
                time.sleep(1)
                newrelation.club = Clubs.objects.latest('created_at')
                
                newrelation.save()
                return redirect('Clubs:list')
            else:
                print(form2.errors)
    else:
        form = forms.CreateClub()
        form2 = forms.CreateClubRelations()
    return render(request, 'Clubs/club_new.html', { 'form': form ,'form2': form2 })
