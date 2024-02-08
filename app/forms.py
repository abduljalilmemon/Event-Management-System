# forms.py
from django import forms


class ImportForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')
