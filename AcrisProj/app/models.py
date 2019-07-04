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
    komisioni = models.ForeignKey(Komisionet)
    vlersuesi = models.ForeignKey(Vlersues)

