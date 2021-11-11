from rest_framework import serializers
from contact.models import *

class Contact_Seriallizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"