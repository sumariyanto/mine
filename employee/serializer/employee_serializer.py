from employee.models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class EmployeeSerializer(serializers.ModelSerializer):
    email =serializers.EmailField(max_length=50, validators=[UniqueValidator(queryset=EmployeeModel.objects.all(),message="Email already used..")])
    nik =serializers.CharField(max_length=25, validators=[UniqueValidator(queryset=EmployeeModel.objects.all(),message="NIK id already used..")])
    phone =serializers.CharField(max_length=25, validators=[UniqueValidator(queryset=EmployeeModel.objects.all(),message="Phone Number already use..")])
    class Meta:
        model = EmployeeModel
        fields = "__all__"