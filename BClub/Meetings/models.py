from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from Books.models import Books

from Clubs.models import Clubs



# Create your models here.
class Meetings(models.Model):
    
    club = models.ForeignKey(Clubs, on_delete=models.SET_DEFAULT, default=1)
    meeting_id = models.AutoField(primary_key=True)
    meeting_name = models.CharField()
    meeting_local = models.CharField()
    meeting_date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Books, on_delete=models.SET_DEFAULT, default=1)
    book_progress_at = models.IntegerField( default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Meetings'
        