from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Members(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField()
    member_phone = models.IntegerField(blank=True, null=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    
    class Meta:
        db_table = 'Members'
