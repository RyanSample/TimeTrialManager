from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=150)
    event_start = models.DateTimeField("Start date time")
    event_end = models.DateTimeField("End date time")
    segment_url = models.URLField()
    distance = models.DecimalField(max_digits=5, decimal_places=2) #km, max of 999.99
    elevation = models.DecimalField(max_digits=6, decimal_places=2) #meters, max 9999.99
