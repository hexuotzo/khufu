from django.db import models
from django import forms

class KhufuForm(forms.Form):
    title = forms.CharField(max_length=100)
    message = forms.CharField()
# Create your models here.
