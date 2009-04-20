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
    #khufuforms    = models.ForeignKey(KhufuForm)
    slug          = models.SlugField(
                     unique_for_date='pub_date',
                     help_text='Automatically built From the title.'
                     )    




    class Meta:
        ordering      = ('-pub_date',)
#        get_latest_by = 'pub_date'
#        db_table      = "blog_entry"


    def get_absolute_url(self):
        return "/hello/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.title)

    def __unicode__(self):
        return self.title

    



# Create your models here.
