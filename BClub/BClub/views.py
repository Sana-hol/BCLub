from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url = '/Members/login')
def homepage(request):
    return render(request, 'home.html')