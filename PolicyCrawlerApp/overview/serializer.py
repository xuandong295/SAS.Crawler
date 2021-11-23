from rest_framework import serializers
from .models import Tblpolicies


class ThreatDetectionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpolicies
        fields = '__all__'