# forms.py
from django import forms
from .models import Participant
from django.forms import Form, TextInput, EmailInput, ModelForm, FileInput


class ImportForm(Form):
    csv_file = forms.FileField(label='Select a CSV file')


class AddParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
            }),
            'phone_number': TextInput(attrs={
                'class': "form-control",
            }),
            'profile_image': FileInput(attrs={
                'class': "form-control",
            })
        }

    def clean_email(self):
        return self.cleaned_data.get('email')
