
from django.db import models

class Route(models.Model):
    start = models.CharField(max_length=500)
    end = models.CharField(max_length=500)
    vehicle = models.CharField(max_length=500)
    cost = models.FloatField(max_length=500)
    time = models.IntegerField()

    def __str__(self):
        return self.start + ' - ' + self.end




