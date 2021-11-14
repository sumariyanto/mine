from django.http.response import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from contact.models import *
from contact.seriallizer import *
from contact.seriallizer.contact_seriallizer import Contact_Seriallizer

class Contact_V1(APIView):
    def get(self,request, format=None):
        id = request.GET.get('id')
        objmodel = Contact.objects.all()

        contactserial =Contact_Seriallizer(objmodel,many=True, context={'request':request})
        return Response({'result':contactserial.data})
        
    def post(self,request,format=None):
       
        if request.user.is_authenticated:
        # Do something for authenticated users.
            user = request.user
            data ={
                'address':request.POST.get('address'),
                'phone':request.POST.get('phone'),
                'userowner':user.id
            }
            objcontact = Contact.objects.all()
            objcontact = objcontact.filter(userowner=user.id)
            total = objcontact.count()
            listuser={
                'user':user.id,
                'username':user.username,
                'total':total,
            }
           
            if int(total)==0:
                hello='ini fungsiku jika 0'
                serializer = Contact_Seriallizer(data=data)     
            else:
                hello='ini jika lebih dari 0'
               
        if serializer.is_valid():
            serializer.save()
            return Response({serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                   
        # return Response({'result':data,'listuser':listuser, 'pesan':hello})
        
        # Do something for anonymous users.

        
        # print(data)
        # objcontact = Contact.objects.all()
        # objcontact = objcontact.filter(userowner=user.id)
        # total = objcontact.count()
        # if int(total) > 0:
        #     pesan = 'Maaf Data Anda sudah ada di contact'
        #     serializer = Contact_Seriallizer(objcontact,many=True)
        #     return Response({'pesan':pesan,'total':total,'result':serializer.data})
        # else:                    
        #     serializer = Contact_Seriallizer(data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response({serializer.data}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ContactDetail_v1(APIView):
    def get_object(self,pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self,request, pk, format=None):
        objcontact = self.get_object(pk)
        seriallizer = Contact_Seriallizer(objcontact)
        return Response(seriallizer.data)