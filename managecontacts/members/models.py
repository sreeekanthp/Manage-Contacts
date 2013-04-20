from django.db import models
from django.utils import timezone

from groups.models import Group


class Member(models.Model):
    '''Creates a model of member consisting of the required fields.'''
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    organisation = models.CharField(max_length=20)
    email = models.EmailField()
    group = models.ForeignKey(Group, null=True, blank=True )

    def __unicode__(self):
        return self.firstname
    
