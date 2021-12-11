from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

class UserMode(APIView):
    def get(self,request):
        dg=User.objects.all()
        
        context={
            'mode':'usermode'
        }
        return Response({'result':context})