from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from datetime import *
import json
from django.db.models import Q,F
from access.views.pagingku import listpageku, pagingku
from django.core.paginator import InvalidPage, Paginator,EmptyPage, PageNotAnInteger
from rest_framework.pagination import _get_displayed_page_numbers as listpage_range
from rest_framework.pagination import *

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

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'limit'
    # page_size_query_param = 'page_size'
    max_page_size = 50
    #url ?page=xx
    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return page_number

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return page_number
   
  
    def get_paginated_response(self, data):  
        return Response(OrderedDict([
             ('pageRange',listpage_range(self.page.number,self.page.paginator.num_pages)),           
             ('perPage',self.page.paginator.per_page),
             ('totalPages', self.page.paginator.num_pages),
             ('totalData', self.page.paginator.count),
             ('currentPage', self.page.number),
             ('nextPage', self.get_next_link()),
             ('previousPage', self.get_previous_link()),
             ('results', data)
         ]))
  

class UserPageOffset(APIView):  
    pagination_class = StandardResultsSetPagination
    serializer_class = UserSerializer   
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator    
    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                self.request, view=self)  

    def get_pagination_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data) 
    
    def get(self, request, format=None, *args, **kwargs):    
        email = request.GET.get('q')
        nid = request.GET.get('id')
        instance = User.objects.get_queryset().order_by('id')
        if email and email !='':
           instance = instance.filter(Q(email__icontains=email)| Q(username__icontains=email))
        if nid and nid !='':
            instance = instance.filter(id=nid)
       
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_pagination_response(self.serializer_class(page,many=True).data)        
        else:
            serializer = self.serializer_class(instance, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserPage(APIView):
    def get(self,request):
        email = request.GET.get('q')
        nid = request.GET.get('id')
        user_list = User.objects.get_queryset().order_by('id')
        if email and email !='':
           user_list = user_list.filter(Q(email__icontains=email)| Q(username__icontains=email))
        if nid and nid !='':
            user_list = user_list.filter(id=nid)
        total_row=user_list.count()
        #---------------------------------------------
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit',5))
        paginator = Paginator(user_list, limit)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        
        # ----------------------------------------------
         # Get the index of the current page
        index = users.number - 1
        # This value is maximum index of your pages, so the last page - 1
        max_index = len(paginator.page_range)
        # You want a range of 7, so lets calculate where to slice the list
        start_index =index - 3 if index >=3 else 0
        end_index = index + 3 if index <= max_index -3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]
       
        # ----------------------------------------------
        # listpage = listpageku(page,paginator.num_pages)
        serial =UserSerializer(users, many=True,context={'request':request})
        return Response({
            
            'total_row':total_row,
            'listpage':page_range,
            'result':serial.data,
            },
            status=status.HTTP_200_OK)


class UserPageList(APIView):
    def get(self,request):
        limit = int(request.GET.get('limit',5))
        offset = request.GET.get('page',1)
       
    
        paginator =Paginator(User.objects.all(),limit)
        
        try:
            page = int(offset)
        except:
            page =1
        try:
            user =paginator.page(page)
        except (EmptyPage,InvalidPage):
            user = paginator.page(1)
        
        # Get the index of the current page
        index = user.number - 1
        # This value is maximum index of your pages, so the last page - 1
        max_index = len(paginator.page_range)
        # You want a range of 7, so lets calculate where to slice the list
        start_index =index - 3 if index >=3 else 0
        end_index = index + 3 if index <= max_index -3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]
        next_page = user.next_page_number()
        prev_page = user.previous_page_number()
        # Get our new page range. In the latest versions of Django page_range returns 
        # an iterator. Thus pass it to list, to make our slice possible again.
        serial =UserSerializer(user,many=True,context={'request':request})
        return Response({

            # 'next_page':next_page,
            # 'prev_page':prev_page,
            # 'record_row':total,
            'index':index,
            'max_index':max_index,
            'page_range':page_range,
            'result':serial.data,
            'start_index':start_index,
            'end_index':end_index,
            'total_page':paginator.num_pages,
        })
