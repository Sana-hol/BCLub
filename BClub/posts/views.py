from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = '/Members/login')
def posts_list(request):
    return render(request, 'posts/posts_list.html')


@login_required(login_url = '/Members/login')
def post_new(request):
    return render(request, 'posts/post_new.html')