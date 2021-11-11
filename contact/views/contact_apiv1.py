from rest_framework.views import APIView
from rest_framework.response import Response
from contact.models import *
from contact.seriallizer import *

class Contact_V1(APIView):
    def get(self,request, format=None):
        id = request.GET.get('id')
        objmodel = Contact.objects.all()

        contactserial = Contact_Seriallizer(objmodel,many=True, context={'request':request})
        return Response({'result':contactserial.data})