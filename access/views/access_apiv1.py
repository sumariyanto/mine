from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from datetime import *
import json
from django.db.models import Q,F
from access.views.pagingku import listpageku, pagingku
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

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

class UserListApi(APIView):       
    def get(self,request,format=None):
        email =request.GET.get('q')
        nid =request.GET.get('id')
       
        user = User.objects.all()
        if email and email !='':
            user = user.filter(Q(email__icontains=email)| Q(username__icontains=email))
        if nid and nid !='':
            user = user.filter(id=nid)
        total = user.count()
        # -----------------------------------------------------------
        
        page_number = self.request.query_params.get('offset',1)
        page_size = self.request.query_params.get('limit',5)
        if page_number !='':
            paginator = Paginator(user, page_size)
        if page_number =='':
            page_number = self.request.query_params.get(1,1)
            paginator = Paginator(user, page_size)
        try:
            users = paginator.page(page_number)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
       

        serializer = UserSerializer(users, many=True, context={'request':request})
        # -----------------------------------------------------------
        num_of_objects = paginator.count
       
        num_of_pages = paginator.num_pages
        list_page = []
        offset = int(page_number)
        page_size = int(page_size)
        if offset >=1:
            list_page.append(1)
        if offset + 3 < num_of_pages:
            for i in range(offset,offset+4):
                list_page.append(i)
        else:
            for i in range(offset,num_of_pages):
                list_page.append(i)
        list_page.append(offset-1)

        if int(num_of_pages)-page_size > 0:
            for i in range(total-page_size,num_of_pages+1):
                list_page.append(i)
        else:
            for i in range(0,num_of_pages+1):
                list_page.append(i)
        list_page =list(set(list_page))
        if 0 in list_page:
            list_page.remove(0)
        list_page.sort()
       #-------------------------------------------
       

        return Response({
            'list_page':list_page,
            'result':serializer.data,
            'total':num_of_objects,
           
            'pages':num_of_pages,
           
        },status=status.HTTP_200_OK)
      
class UserPage(APIView):
    def get(self,request):
        user_list = User.objects.all()
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit',10)
        paginator = Paginator(user_list, limit)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        total =paginator.num_pages
        listpage = listpageku(page,total)
        serial =UserSerializer(users, many=True,context={'request':request})
        return Response({'listpage':listpage,'result':serial.data},status=status.HTTP_200_OK)