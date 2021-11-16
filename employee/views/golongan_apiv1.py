from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from employee.models import *
from employee.serializer.bgn_dan_gol_serializer import *


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
