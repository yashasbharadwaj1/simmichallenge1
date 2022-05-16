from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Contact(models.Model):
   
    Name = models.CharField(max_length=25)
    City = models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    Createdate = models.DateTimeField(default=timezone.now)
    Phonenumber = models.CharField(max_length=20)
    Email=models.EmailField( max_length=254)
    

    
    class Meta:
        ordering = ('-Createdate',)
    
    
    #By default, the result is sorted ascending (the lowest value first), to change the direction to descending (the highest value first), use the minus sign (NOT), - in front of the field name:
    def __str__(self):
        return self.Name 
