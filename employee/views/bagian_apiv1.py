from os import stat
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from employee.models import *
from employee.serializer.bgn_dan_gol_serializer import *

class BagianList_Apiv1(APIView):
    def get(self,request):
        bagian = BagianModel.objects.all()
        serializerobj = BagianSerializer(bagian, many=True,context={'request':request})
        return Response({'result':serializerobj.data}, status=status.HTTP_200_OK)

    def post(self,request, format=None):
        obj_serializer = BagianSerializer(data=request.data)
        if obj_serializer.is_valid():
            obj_serializer.save()
            return Response(obj_serializer.data,status=status.HTTP_201_CREATED)
        return Response({'result':obj_serializer.errors},status=status.HTTP_409_CONFLICT)

class BagianDetail_Apiv1(APIView):
    def get_object(self,pk):
        try:
            return BagianModel.objects.get(pk=pk)
        except BagianModel.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,format=None):
        objmodel = self.get_object(pk)
        serializerobj = BagianSerializer(objmodel)
        return Response(serializerobj.data)

    def put(self, request, pk, format=None):
        objmodel = self.get_object(pk)
        objserial = BagianSerializer(objmodel,data=request.data)

        if objserial.is_valid():
            objserial.save()
            return Response(objserial.data, status=status.HTTP_200_OK)
        return Response(objserial.errors,status=status.HTTP_400_BAD_REQUEST)