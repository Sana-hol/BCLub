from django.urls import path
from . import views

app_name = 'Meetings'

urlpatterns = [
    path('<int:club_id>/manage/new-meeting', views.meeting_new, name="meet"),
    
]
