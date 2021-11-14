from django.http.response import Http404
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
        objmodel = EmployeeModel.objects.all().order_by('id')
       
        if cari and cari !='':
            objmodel = objmodel.filter(Q(fullname__icontains=cari))
        
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

       
        objmodel_serializer = EmployeeSerializer(objmodel, many=True,context={'request':request})
        return Response({'result':objmodel_serializer.data,'total':total_row})

    def post(self,request, format=None):
        data ={
            'fullname':request.POST.get('fullname'),
            'email' :request.POST.get('email'), 
            'phone' :request.POST.get('phone'),
            'nik':request.POST.get('nik'),
            'gender':request.POST.get('gender'),
            'address':request.POST.get('address'),
            'city':request.POST.get('city'),
            'provinsi': request.POST.get('provinsi'),
            'staf': request.POST.get('staf'),
        }
        email = data['email']
        nik = data['nik']
        objmodel =EmployeeModel.objects.filter(Q(email=email) | Q(nik=nik))
        if(objmodel.count()) >0:
            pesan ="Ditemukan data email atau  nik yang sudah terdafatar"
            return Response({'pesan':pesan})
        else:
            obj_serializer = EmployeeSerializer(data=data)
            if obj_serializer.is_valid():
                obj_serializer.save()
                return Response(obj_serializer.data,status=status.HTTP_201_CREATED)
            return Response(obj_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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
        snippet = self.get_object(pk)
        serializer = EmployeeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)