from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
ROLE={
    ("1", "Read"),
    ("2", "ReadWrite"),
    ("3", "Full"),
}
class Contact(models.Model):    
    address = models.CharField(max_length=100, blank=True)    
    nohp = models.CharField(max_length=25,blank=True)
    role = models.CharField(max_length=10,choices=ROLE,default=1)
    phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField()
    userowner = models.ForeignKey(User, on_delete=CASCADE, blank=True)
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.email