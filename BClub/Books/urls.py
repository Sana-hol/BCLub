from django.urls import path
from . import views

app_name = 'Books'

urlpatterns = [
    path('', views.book_list, name="list"),
    path('<int:book_id>', views.book_page, name="page"),
]