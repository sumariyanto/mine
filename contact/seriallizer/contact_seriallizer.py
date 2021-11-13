from django.http import request
from rest_framework import serializers
from contact.models import *
from contact.seriallizer import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
class Contact_Seriallizer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = "__all__"
    
    