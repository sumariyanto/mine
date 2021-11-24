from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from datetime import *


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

