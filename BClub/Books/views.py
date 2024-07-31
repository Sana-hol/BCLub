
from django.shortcuts import render
from .models import Books
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = '/Members/login')
def book_list(request):
    books = Books.objects.all()
    return render(request, 'Books/book_list.html', {'Books': books})

@login_required(login_url = '/Members/login')
def book_page(request, book_id):
    book = Books.objects.get(book_id=book_id)
    return render(request, 'Books/book_page.html', {'book': book})
