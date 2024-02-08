from django.contrib import admin
from .models import Event, User, Staff, Participant, Participation

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Participant)
admin.site.register(Participation)
# Register your models here.
