
from django.core import paginator
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from contact.seriallizer import *
from django.db.models import Q,F
from django.http import Http404
from django.core.paginator import *


class AddRegisterUser(APIView):
    def get(self,request):
        cari=request.GET.get('q')
        nid = request.GET.get('id')
        limit = int(request.GET.get('limit',5))
        offset = int(request.GET.get('offset',0))
       
        objmodel=User.objects.get_queryset().order_by('id')
        if request.user.is_authenticated:
            user = request.user
            obuser = User.objects.filter(username=user)
            
            iduser =[]
            for row in obuser:
                idata ={
                    'is':row.id,
                    'nameuser':row.username,
                    'is_active':row.is_active,
                    'first_name':row.first_name,
                    'last_name':row.last_name,
                }
                iduser.append(idata)
            
        if nid:
            objmodel = objmodel.filter(id=nid)
        if cari and cari !='':
            objmodel = objmodel.filter(Q(first_name__icontains=cari))
        paginator=Paginator(objmodel,limit)

        try:
            users = paginator.page(offset)
        except PageNotAnInteger:
            users = paginator.page(1)
        # except EmptyPage:
        except(EmptyPage, InvalidPage):
            users = paginator.page(paginator.num_pages)
        total_page=paginator.num_pages
        per_page=paginator.per_page
        index = users.number - 1
        total_row = users.paginator.count
        if users.has_previous()==True and users.has_next()==True:
            page_next = users.next_page_number()
            page_prev = users.previous_page_number()
        else:
            page_prev = None
            page_next = None
        page_range=paginator.get_elided_page_range(users.number,on_each_side=3, on_ends=2)
        pagination={
                'first':users.start_index(),
                'next':page_next,
                'page_range':page_range,
                'prev':page_prev,
                'end':users.end_index(),
            }
           
           
       
      
        serializer=UserSerializer(users,many=True,context={'request':request})
        return Response({'page':pagination,'result':serializer.data,'total':total_row,'useractive':iduser,})

    def post(self, request, format=None):
        objserializer = UserSerializer(data=request.data)
        if not objserializer.is_valid():
            return Response(objserializer.errors, status=400)
        objserializer.save()
        return Response(objserializer.data)
       
class DetailUser(APIView):
    def get_object(self, pk):
         try:
             return User.objects.get(pk=pk)
         except User.DoesNotExist:
             raise Http404
     
    def put(self, request, pk, format=None):
         user = self.get_object(pk)
         serializer = UserSerializer(user, data=request.DATA)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
         user = self.get_object(pk)
         user.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
