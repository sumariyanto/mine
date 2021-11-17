from copy import error
from django.http.response import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from employee import serializer
from employee.models import *
from django.db.models import Q,F,Count
from employee.serializer.employee_serializer import *
from rest_framework import status



class EmployeeListView(APIView):
    def get(self,request,format=None):
        limit = int(request.GET.get('limit',10))
        offset = int(request.GET.get('offset',0))
        cari = request.GET.get('q')
        st_staf = request.GET.get('status')
        objmodel = EmployeeModel.objects.all().order_by('id')
       
        if cari and cari !='':
            objmodel = objmodel.filter(Q(fullname__icontains=cari))
        if st_staf and st_staf != '':
            objmodel = objmodel.filter(staf=int(st_staf))

        total_row = objmodel.count()
        if limit:
            if offset:
                if int(offset)>0:
                    objmodel = objmodel[int(offset):int(limit)+int(offset)]
                else:
                    objmodel = objmodel[int(offset):int(limit)]
            else:
                objmodel = objmodel[0:int(limit)]
        else:
            objmodel = objmodel[0:10]

        list_page=[]
        if offset >=1:
            list_page.append(1)
        if offset+3 < total_row:
            for i in range(offset, offset+4):
                list_page.append(i)
        else:
            for i in range(offset,total_row):
                list_page.append(i)
        list_page.append(offset-1)

        if total_row-3 > 1:
            for i in range(total_row-3, total_row+1):
                list_page.append(i)
        else:
            for i in range(1,total_row+1):
                list_page.append(1)
        list_page = list(set(list_page))
        if 0 in list_page:
            list_page.remove(0)
        list_page.sort()  

        objmodel_serializer = EmployeeSerializer(objmodel, many=True,context={'request':request})
        return Response({'result':objmodel_serializer.data,'total':total_row,'page':list_page})

    def post(self,request, format=None):
           
        obj_serializer = EmployeeSerializer(data=request.data)
        if obj_serializer.is_valid():
            obj_serializer.save()
            return Response(obj_serializer.data,status=status.HTTP_201_CREATED)
        return Response({'result':obj_serializer.errors},status=status.HTTP_409_CONFLICT)
           

class EmployeeDetailView(APIView):
    def get_object(self,pk):
        try:
           return EmployeeModel.objects.get(pk=pk)
        except EmployeeModel.DoesNotExist:
            raise Http404
        
    def get(self,request, pk, format=None):
        objcontact = self.get_object(pk)
        seriallizer = EmployeeSerializer(objcontact)
        return Response(seriallizer.data)
    
    def put(self, request, pk, format=None):
        objemployee = self.get_object(pk)   
        serializer = EmployeeSerializer(objemployee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)