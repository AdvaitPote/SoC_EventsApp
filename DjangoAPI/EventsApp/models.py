from django.db import models

# Create your models here.
class Events(models.Model):
    EventId = models.AutoField(primary_key=True)
    EventName = models.CharField(max_length=100)
    DateOfEvent = models.DateField()
    TimeOfEvent = models.TimeField()

