import datetime

from django.db import models
from django.utils import timezone
from contracts.models import Contract


class Contact(models.Model):
    '''Creates a model of the application to add contact having fields Firstname, Lastname\
    etc and creates a field contract having the foriegnkey of model Contract, to link\
    contact and contract  '''
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    contract = models.ForeignKey(Contract, null=True, blank=True)

    def __unicode__(self):
        return self.firstname


