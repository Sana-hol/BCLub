from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms, models
from .models import Members

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("Members:config")
    else:
        form = UserCreationForm()
    return render(request, "Members/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if Members.objects.filter(account=request.user) == None:
                return redirect("Members:config")
            elif "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("/")
    else: 
        form = AuthenticationForm()
    return render(request, "Members/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')

@login_required(login_url = '/Members/login')
def member_config(request):
    if request.method == "POST":
        form = forms.ConfigMember(request.POST)
        if form.is_valid():
            newmember = form.save(commit=False)
            newmember.account = request.user
            newmember.save()
            return redirect("/")
    else:
        form = forms.ConfigMember()
    return render(request, 'Members/member_conf.html', {'form':form})