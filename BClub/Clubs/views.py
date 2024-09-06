
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
def clubs_list(request):
    clubs = Clubs.objects.all()
    return render(request, 'Clubs/clubs_list.html', {'Clubs': clubs})

@login_required(login_url = '/Members/login')
def club_page(request, club_id):
    club = Clubs.objects.get(club_id=club_id)
    membersinclub = ClubStatus.objects.filter(club=club_id).iterator()
    members = []
    for member in membersinclub:
        memb = Members.objects.filter(member_id=member.member_id).values()
        members.append(memb)
    return render(request, 'Clubs/club_page.html', {'Club': club, 'Members': members})

@login_required(login_url = '/Members/login')
def add_member(request, club_id):
    if request.method == 'POST': 
        form = forms.CreateClubRelationsAddMembers(request.POST)
        if form.is_valid():
            addmember = form.save(commit=False)
            addmember.club = Clubs.objects.get(club_id = club_id)
            addmember.save()
            return redirect('Clubs:page', club_id )
        else:
            print(form.errors)
    else:
        form = forms.CreateClubRelationsAddMembers()
    return render(request, 'Clubs/add_member.html', {'form': form , 'club_id':club_id })

@login_required(login_url = '/Members/login')
def set_book(request, club_id):
    currentclub = Clubs.objects.get(club_id = club_id)
    currentclubinitialsprogress = Clubs.objects.filter(club_id = club_id).values('current_progress')[0]
    currentbookinclub = Clubs.objects.get(club_id = club_id).current_book
    currentbook = Books.objects.filter(book_id = currentbookinclub.book_id).values(current_book=F('book_title'))[0]
    currentclubinitials = currentbook | currentclubinitialsprogress
    print(currentclubinitials)
    form = forms.SetBook(request.POST or None, instance=currentclub, initial = currentclubinitials)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Clubs:page', club_id )
        else:
            print(form.errors)
    return render(request, 'Clubs/set_book.html', {'form': form, 'club_id':club_id})


@login_required(login_url = '/Members/login')
def manage_club(request, club_id):
    Club = Clubs.objects.get(club_id = club_id)
    if request.user == Club.club_admin:
        print('sucess')
        return render(request, 'Clubs/club_manage.html' , {'club_id':club_id })
    else:
        print('fail')
        messages.success(request, "Você não é o adm desse clube!!!!")
        return redirect('Clubs:page', club_id )
    
    

@login_required(login_url = '/Members/login')
def club_new(request): 
    if request.method == 'POST': 
        form = forms.CreateClub(request.POST) 
        form2 = forms.CreateClubRelations(request.POST)
        if form.is_valid():
            newclub = form.save(commit=False)
            newclub.club_admin = request.user 
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

        
            