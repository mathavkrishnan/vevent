from django.db import models
class regevents(models.Model):
    user = models.CharField(max_length=255)
    eventname = models.CharField(max_length=255)
    link = models.URLField(max_length=100)
    location = models.CharField(max_length=100)
    eventdate = models.DateField()
    time = models.TimeField(null=False)