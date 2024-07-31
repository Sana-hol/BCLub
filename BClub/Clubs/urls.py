from django.urls import path
from . import views

app_name = 'Clubs'

urlpatterns = [
    path('', views.clubs_list, name="list"),
    path('<int:club_id>/', views.club_page, name="page"),
    path('new-club/', views.club_new, name="new"),
    path('<int:club_id>/add', views.add_member, name="add"),
    
]