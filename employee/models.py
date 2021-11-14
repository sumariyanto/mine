from datetime import datetime
from django.db import models
from django.db.models.fields import EmailField, GenericIPAddressField
from django.db.models.query_utils import check_rel_lookup_compatibility

# Create your models here.
GENDER =(
    (1,'Pria'),
    (2,'Wanita'),
)
STATUSSTAF =(
    (1,'Tetap'),
    (2,'Kontrak'),
    (3,'Percobaan'),
    (4,'Harian'),
)
class EmployeeModel(models.Model):
    fullname = models.CharField(max_length=50,blank=True,null=False)
    email = models.EmailField(max_length=50,blank=False,null=False)
    phone = models.CharField(max_length=30,blank=False,null=False)
    nik = models.CharField(max_length=50,blank=False,null=False)
    gender = models.CharField(max_length=15, choices=GENDER, default=1)
    address = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=50,blank=True)
    provinsi = models.CharField(max_length=50,blank=True)
    staf= models.CharField(max_length=15,choices=STATUSSTAF)

    def __str__(self):
        return self.email

    
