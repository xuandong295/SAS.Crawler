from rest_framework import serializers
from .models import Tblapis


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblapis
        fields = '__all__'