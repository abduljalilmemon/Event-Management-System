from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    location = models.TextField()
    max_participants = models.IntegerField(default=100)

    def __str__(self):
        return self.name