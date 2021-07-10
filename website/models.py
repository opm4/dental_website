from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    
    def __str__(self):
        return '%s - %s - %s%s' %(self.name, self.stage, self.currency, self.price)