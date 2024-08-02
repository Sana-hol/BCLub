from django.urls import path
from . import views

app_name = 'Clubs'

urlpatterns = [
    path('', views.clubs_list, name="list"),
    path('<int:club_id>/', views.club_page, name="page"),
    path('new-club/', views.club_new, name="new"),
    path('<int:club_id>/manage/add', views.add_member, name="add"),
    path('<int:club_id>/manage/set', views.set_book, name="set"),
    path('<int:club_id>/manage', views.manage_club, name="manage"),
    
]
