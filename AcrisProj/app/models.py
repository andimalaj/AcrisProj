"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
#from django.conf import settings
#from django.contrib.auth import get_user_model

# Create your models here.

class Komisionet(models.Model) :
    emertimi = models.CharField(max_length = 250)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
         return self.emertimi



class Vlersues(models.Model) :
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
         return self.userid.email


class KomisionetV(models.Model):
    komisioni = models.ForeignKey(Komisionet , on_delete=models.CASCADE)
    vlersuesi = models.ForeignKey(Vlersues , on_delete=models.CASCADE)


class ScopusKatalog(models.Model) :
    scopusid = models.CharField(max_length = 250,default=None, blank=True, null=True)
    pubmedid = models.CharField(max_length = 250,default=None, blank=True, null=True)
    author = models.CharField(max_length = 250,default=None, blank=True, null=True)
    affiliation = models.CharField(max_length = 250,default=None, blank=True, null=True)
    citation_count = models.CharField(max_length = 250,default=None, blank=True, null=True)
    title = models.CharField(max_length = 250,default=None, blank=True, null=True)
    issn = models.CharField(max_length = 250,default=None, blank=True, null=True)
    date = models.CharField(max_length = 250,default=None, blank=True, null=True)
    journal = models.CharField(max_length = 250,default=None, blank=True, null=True)
    snip = models.CharField(max_length = 250,default=None, blank=True, null=True)
    sjr = models.CharField(max_length = 250,default=None, blank=True, null=True)
    citescore = models.CharField(max_length = 250,default=None, blank=True, null=True)