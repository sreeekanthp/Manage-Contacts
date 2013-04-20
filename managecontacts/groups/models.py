import datetime

from django.db import models


class Group(models.Model):
    '''Creates the model of Group containig the required fields to add details.'''
    group_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.group_code

