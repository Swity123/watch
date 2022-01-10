from django import forms
from django.forms import fields
from .models import *
from django.conf import settings

class watchform(forms.ModelForm):
    class Meta:
        model = watches

        fields = ['watch_type','brand_name','price','des']