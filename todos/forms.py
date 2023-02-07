from django.forms import ModelForm
from django import forms 
from .models import *

"""
Django form for inputing the Todos

"""

class EntryForm(ModelForm):
   
    class Meta:
        model = Entry
        fields = '__all__'
        exclude = ("completed", )
        widgets = {
                    'title':forms.TextInput(attrs={'class':'title_class',"placeholder":"title", "label":""}) ,
                    'body':forms.Textarea(attrs={'class':'body_class'}) ,
           
                }
            
