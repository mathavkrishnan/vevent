from email.policy import default
from pickle import TRUE
from pyexpat import model
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser,User
class user(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_club = models.BooleanField(default=True)
class events(models.Model):
    eventname = models.CharField(max_length=255)
    link = models.URLField(max_length=100)
    lastdate = models.DateField()
    eventdate = models.DateField()
    poster = models.ImageField(upload_to = 'clubmembers/images/')
    time = models.TimeField()
    location = models.CharField(max_length=100)
    slots = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,db_constraint=False,default=False)