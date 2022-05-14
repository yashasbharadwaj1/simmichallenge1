from django.db import models
class Contact(models.Model):
    Name = models.CharField(max_length=25)
    City = models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    Createdate = models.DateTimeField(auto_now_add=True)
    Phonenumber = models.CharField(max_length=20)
    Email=models.EmailField( max_length=254)
    class Meta:
        ordering = ('-Createdate',)
    
    
    #By default, the result is sorted ascending (the lowest value first), to change the direction to descending (the highest value first), use the minus sign (NOT), - in front of the field name:
    def __str__(self):
        return self.Name