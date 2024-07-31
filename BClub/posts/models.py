from django.db import models
from django.contrib.auth.models import User
from Books.models import Books
from Clubs.models import Clubs
from Members.models import Members

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    club_id = models.ForeignKey(Clubs, on_delete=models.DO_NOTHING)
    member_id = models.ForeignKey(Members, on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey(Books, on_delete=models.DO_NOTHING)
    quote = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    progress_wposted = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'
        managed=False