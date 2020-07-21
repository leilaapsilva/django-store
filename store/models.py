import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    creation_date = models.DateTimeField('creation date', null=True)
    description = models.CharField(max_length=1000, null=True)
    image = models.FileField(upload_to = 'products/')

    def __str__(self):
        return self.name

    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)    
