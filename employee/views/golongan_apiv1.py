from django.core import exceptions
from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from employee.models import *
from employee.serializer.bgn_dan_gol_serializer import *
from django.contrib.auth import authenticate


class GolonganList_Apiv1(APIView):
    def get(self,request):
        golongan = GolonganModel.objects.all()
        total_row = golongan.count()


        serializer = GolonganSerializer(golongan,many=True,context={'request':request})
        return Response({'result':serializer.data})
    def post(self,request,format=None):
        golongan = GolonganSerializer(data=request.data)
        if golongan.is_valid():
            golongan.save()

            return Response({'result':golongan.data},status=status.HTTP_201_CREATED)
        return Response(golongan.errors, status=status.HTTP_400_BAD_REQUEST)

class GolonganDetail_Apiv1(APIView):
    def get_object(self,pk):
        try:
            return GolonganModel.objects.get(pk=pk)
        except GolonganModel.DoesNotExist:
            raise Http404
    def get(self,reques,pk):
        objmodel = self.get_object(pk)
        serializer = GolonganSerializer(objmodel)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        
        objmodel = self.get_object(pk)
        serializer = GolonganSerializer(objmodel,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        objmodel =self.get_object(pk)
        if request.user.is_superuser == True:
            data ={
                "pesan":request.user.is_active,
                "user":request.user.is_superuser
            }
            
        else:
            data ={
                "user":request.user.username,
                "level":request.user.is_staff,
            }
           
        return Response(data)