from django import forms
from django.forms import ModelForm
from .models import ContactModel


class CONTACTFORM(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'subject','email', 'messagess')
        exclude = ['created']

