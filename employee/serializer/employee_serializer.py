from django.http import response
from django.http.response import JsonResponse
from django.utils.translation import deactivate_all
from rest_framework.response import Response
from employee.models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class EmployeeSerializer(serializers.ModelSerializer):
    email =serializers.EmailField(max_length=50, validators=[UniqueValidator(queryset=EmployeeModel.objects.all(),message="Email already used..")])
    nik =serializers.CharField(max_length=25, validators=[UniqueValidator(queryset=EmployeeModel.objects.all(),message="NIK id already used..")])
    phone =serializers.CharField(max_length=25, validators=[UniqueValidator(queryset=EmployeeModel.objects.all(),message="Phone Number already use..")])
    staf = serializers.CharField(source="get_staf_display")
    detail= serializers.SerializerMethodField(read_only=True)
    def get_detail(self,obj):
        
        golongan ={
            'id':obj.golongan.id if obj.golongan is not None else '',
            'golongan':obj.golongan.golongan if obj.golongan is not None else '',
            'keterangan':obj.golongan.info if obj.golongan is not None else '',
        },
        bagian = {
            'id':obj.bagian.id if obj.bagian is not None else '',
            'bagian':obj.bagian.bagian if obj.bagian is not None else '',
            'keterangan':obj.bagian.info if obj.bagian is not None else '',
        }
        return ({'golongan':golongan,'bagian':bagian})
            
      

    class Meta:
        model = EmployeeModel
        fields = ['id','fullname','nik','email','phone','gender','address','city','provinsi','staf','golongan','bagian','detail']