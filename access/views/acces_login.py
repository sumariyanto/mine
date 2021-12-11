from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import *
from django.core.checks import messages
from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework import permissions
from rest_framework.response import Response

import json

from contact.seriallizer.user_seriallizer import UserSerializer
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    # permission_classes = [IsAuthenticated|ReadOnly]
    def get(self,request):
        if request.user=='':
            user=User.objects.get(id=request.user.id)
            serial=UserSerializer(user)
            return Response(serial.data)
        else:
            return Response({'pesan':request.user.id})
        


    
    def post(self,request,format=None):
        
        data=json.loads(request.body)
        email=data['emailuser']
        password=data['password']
        variabel={
            'user':email,
            'password':password
            }
        try:
            userfield = User.objects.get(username=email)
            if userfield.check_password(password):
                username = userfield.username
                user = authenticate(username=username, password=password)
                login(request, user)
                pesan={
                   'success':request.user.username
                }
                # return data
               
                # pesan =username
                
            else:
                pesan="Login invalid"
               
        except User.DoesNotExist:
            pass
            pesan ="user DoesNot Exist"
        return Response({'result':pesan})


class UserLogout(APIView):
    # permission_classes = (permissions.AllowAny,)
    def get(self,request):
        logout(request)
        pesan='logut success'
        return Response(pesan)