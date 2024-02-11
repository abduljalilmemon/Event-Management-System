from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


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
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    time = models.DateTimeField()
    location = models.TextField()
    max_participants = models.IntegerField(default=100)
    posted_by = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


def get_profile_image_filepath(self, filename):
    return 'app/images/profile_images/' + str(self.pk) + '/profile_image.png'


def get_default_profile_image():
    return "app/images/person_2.jpg"


class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]


class Participation(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
