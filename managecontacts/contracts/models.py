import datetime

from django.db import models
from django.utils import timezone

 
class Contract(models.Model):
    '''Creates a model of the application to add contract having fields\
    Fromdate, Todate etc '''
    from_date = models.DateField()
    to_date = models.DateField()
    list_size = models.IntegerField()
    total_email = models.IntegerField()

    def __unicode__(self):
        return str(self.from_date)



