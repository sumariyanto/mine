
from os import error
from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.http.response import Http404
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import validators
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import *



class UserSerializer(serializers.ModelSerializer):
    # username = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all(),message="username already used..")])
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all(),message="Email already used..")])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('id','username','password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'username':{'required':False},
            'first_name':{'required': True},
            'last_name':{'required': True},

        }

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all(),message="Email already used..")])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields=['username','email','password','password2','first_name','last_name']
        extra_kwargs={
            'password':{'write_only':True},
            'username':{'required':False},
            'first_name':{'required': True},
            'last_name':{'required': True},
        }
    def save(self):
        user=User(
            username=self.validated_data['email'].lower(),
            email=self.validated_data['email'].lower(),
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password =self.validated_data['password']
        password2 =self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({'password':'Password must be match'})
        user.set_password(password)
        user.save()
        return user