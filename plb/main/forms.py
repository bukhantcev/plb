from datetime import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import CharField, TextInput, SelectDateWidget, Select, ModelChoiceField
from django.forms.widgets import ChoiceWidget
from django.utils.deconstruct import deconstructible

from .models import Klients, Zapis, Uslugi



@deconstructible
class PhoneValidator:
    ALLOWED_CHARS = '+1234567890-'
    code = 'digit'


    def __init__(self, message=None):
        self.message = message if message else "Номер должен состоять из цифр и начинаться на '+7' или '8'"

    def __call__(self, value,  *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)



class ZapisForm(forms.ModelForm):
    client_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-custom"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-custom"}), max_length=12)
    class Meta:
        model = Zapis
        fields = ['client_name', 'phone']

    def clean_phone(self):

        phone = self.cleaned_data['phone']
        ALLOWED_CHARS = '+1234567890-'


        if not (set(phone) <= set(ALLOWED_CHARS)):
            raise ValidationError("Номер должен состоять из цифр")
        elif not ("+7" in phone[:2] or "8" == phone[0]):
            raise ValidationError("Номер должен начинаться на '+7' или '8' и состоять из 10 цифр, не считая кода страны")
        else:
            return phone









class KlientsForm(forms.ModelForm):

    name = CharField(empty_value='erer')
    phone = CharField(min_length=11, max_length=12, empty_value='hhfhfhh')

    class Meta:
        model = Klients
        fields = ['name', 'phone']




