from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)


class Staff(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    dob = models.DateField(default='1990-01-01')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    location = models.TextField()
    max_participants = models.IntegerField(default=100)
    posted_by = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
