from django.db import models
from django import forms

class KhufuForm(models.Model):
    title = forms.CharField(max_length=100)
    message = forms.CharField(max_length=100)
    
    def __unicode__(self):
        return self.title



class Entry(models.Model):
    title         = models.CharField(max_length=200)
    pub_date      = models.DateTimeField('date published',blank=True)
#    content       = models.TextField()
#    slug          = models.SlugField(
#                  unique_for_date='pub_date',
#                  help_text='Automatically built From the title.'
#                  )
#    summary       = models.TextField(help_text="One paragraph. Don't add tag.")



# Create your models here.
