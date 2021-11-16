from rest_framework import serializers
from rest_framework import validators
from employee.models import *
from rest_framework.validators import UniqueValidator

class BagianSerializer(serializers.ModelSerializer):
    bagian = serializers.CharField(max_length=35, validators=[UniqueValidator(queryset=BagianModel.objects.all(), message="Already Use")])
    class Meta:
        model = BagianModel
        fields = "__all__"

class GolonganSerializer(serializers.ModelSerializer):
    golongan = serializers.CharField(max_length=35, validators=[UniqueValidator(queryset=GolonganModel.objects.all(), message="Already Use")])
    class Meta:
        model = GolonganModel
        fields = "__all__"