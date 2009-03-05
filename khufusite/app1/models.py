from django.db import models
from django import forms

class KhufuForm(models.Model):
    title = forms.CharField(max_length=100)
    message = forms.CharField(max_length=100)
    
    def __unicode__(self):
        return self.title
# Create your models here.
