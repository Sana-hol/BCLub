from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from Members.models import Members




class Clubs(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField()
    club_admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Clubs'
        
class ClubStatus(models.Model):
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Clubs, default=1, on_delete=models.CASCADE, blank=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE, blank=True)
    club_status = models.IntegerField(default=1)

    class Meta:
        db_table = 'ClubStatus'
        


