#workouts_app/models.py
from django.db import models

class Workout(models.Model):
    name = models.CharField(max_length=40)
    sets = models.SmallIntegerField()
    description = models.TextField()
    creator = models.CharField(max_length=40)
                
    # Below we want to create a display and this will be helpful when we want to view in our admin panel
    def __str__(self):
        return self.name

