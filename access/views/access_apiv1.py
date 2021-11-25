from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from datetime import *
import json

class AccessListApi(APIView):
   def get(self,request):
        if request.user.is_superuser==True:
            data={
                'modul':'lembur',
                'user':request.user.id
            }
        else:
            data={
                'pesan':'no full access',
                'user':request.user.id,
                'user name':request.user.is_staff,
                'tanggal':date.today(),
                'time':datetime.now()
            }
        return Response({'result':data})
class AccessDetailApi(APIView):
    def get(self,request,pk):
        data ={
            "modul":"Access Detail",
            "Method":pk,
        }
        return Response(data)

class AccessPostApi(APIView):
    def post(self,request,format=None):
        # djson={"email":"sdfa@gmail.com","nama":"agung"}
        data=json.loads(request.body.decode("utf-8")) 
        # data =json.loads(request.data["formData"])
        x=data["formData"]
       
        email=x['email'].lower()
        nama=x['nama'].lower()
        fullname=x['fullname'].lower()
        phone=x['phone'].string()
        data={
            'email':email,
            'nama':nama,
            'fullname':fullname,
            'phone':phone
        }
        print(x)
        print(data)
        return Response({'result':data,'json':x})
    def get(self,request,format=None):
        djson='{"email":"sdfa@gmail.com","nama":"agung"}'
        data =json.loads(djson)
        print(data)
        return Response(data)
        
       