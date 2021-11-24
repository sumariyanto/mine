
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
from django.contrib.auth.password_validation import validate_password



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
            'last_name':{'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        # if attrs['username'] != attrs['email']:
        #      raise serializers.ValidationError({"username": "fields didn't match with email fileds."})
        
        return attrs

    def create(self, validated_data):
        try:
            user = User.objects.create(
                username= validated_data['email'].lower(),
                email=validated_data['email'].lower(),
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            
            user.set_password(validated_data['password'])
            return user
       
        except:
            
            raise serializers.ValidationError({"error": status.HTTP_500_INTERNAL_SERVER_ERROR})
    