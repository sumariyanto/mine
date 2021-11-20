from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import *

class TestList_(APIView):
    def get(self,request):
        wel = {
            'judul':'Modul HRD'
        }
        return Response({'result':wel})

class Lembur_list(APIView):
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