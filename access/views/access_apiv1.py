from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from datetime import *
import json
from django.db.models import Q,F
from access.views.pagingku import listpageku, pagingku

from contact.seriallizer.user_seriallizer import UserSerializer

            
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
        phone=x['phone']
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
        email =request.GET.get('q')
        nid =request.GET.get('id')
        limit =request.GET.get('limit',10)
        offset =request.GET.get('offset',0)
        user =User.objects.all()
        if email and email !='':
            user = user.filter(Q(email__icontains=email)| Q(username__icontains=email))
        if nid and nid !='':
            user = user.filter(id=nid)
        total = user.count()
        user = pagingku(limit,offset,user)
        listpage = listpageku(offset,total)
        serialuser = UserSerializer(user,many=True, context={'request':request})
        return Response({'result':serialuser.data,'total':total,'page':listpage},status=status.HTTP_200_OK)
        
       