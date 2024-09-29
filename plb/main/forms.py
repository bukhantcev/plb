from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField

from .models import Klients, Zapis, Uslugi






class ZapisForm(forms.ModelForm):
    client_name = CharField(empty_value='erer')
    phone = CharField(min_length=11, max_length=12, empty_value='hhfhfhh')
    class Meta:
        model = Zapis
        fields = ['client_name', 'phone']


class KlientsForm(forms.ModelForm):

    name = CharField(empty_value='erer')
    phone = CharField(min_length=11, max_length=12, empty_value='hhfhfhh')

    class Meta:
        model = Klients
        fields = ['name', 'phone']

