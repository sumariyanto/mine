from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.fields import EmailField, GenericIPAddressField
from django.db.models.query_utils import check_rel_lookup_compatibility

# Create your models here.
GENDER =(
    ('1','Pria'),
    ('2','Wanita'),
)
STATUSSTAF =(
    ('1','Tetap'),
    ('2','Kontrak'),
    ('3','Percobaan'),
    ('4','Harian'),
)
   
class GolonganModel(models.Model):
    golongan=models.CharField(max_length=25, null=False, blank=False)
    info = models.TextField(max_length=250,blank=False,null=False)

    def __str__(self):
        return self.golongan

class BagianModel(models.Model):
    bagian=models.CharField(max_length=50,blank=False,null=False)
    info=models.TextField(max_length=250,blank=False,null=False)
    def __str__(self):
        return self.bagian

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
    golongan = models.ForeignKey(GolonganModel,on_delete=models.CASCADE,default="1")
    bagian = models.ForeignKey(BagianModel, on_delete=models.CASCADE,default="1")
   

    def __str__(self):
        return self.email

 

  