# forms.py
from django import forms
from .models import Participant


class ImportForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')


class AddParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
