from django.forms import ModelForm
from django import forms 
from .models import *


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
        exclude = ("completed", )
      
