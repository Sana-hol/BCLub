from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_cover = models.ImageField(blank=True, null=True)
    book_title = models.CharField()
    book_author = models.CharField()
    book_rating = models.IntegerField(blank=True, null=True)
    total_size = models.IntegerField(default= 1000, blank=True, null=True)

    class Meta:
        db_table = 'Books'

class Bookstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('Books', on_delete=models.CASCADE, related_name='%(class)s_requests_created')
    member_id = models.IntegerField()
    book_rate = models.IntegerField(blank=True, null=True)
    book_progress = models.IntegerField()

    class Meta:
        db_table = 'BookStatus'
