from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Contact(models.Model):    
    address = models.CharField(max_length=100, blank=False)    
    phone = models.CharField(max_length=20,blank=True)
    userowner = models.ForeignKey(User, on_delete=CASCADE)
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.address