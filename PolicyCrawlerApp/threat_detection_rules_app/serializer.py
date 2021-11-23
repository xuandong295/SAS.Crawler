from rest_framework import serializers
from .models import Tblpolicies


class ThreatDetectionRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpolicies
        fields = ['id', 'name', 'cloudtype', 'severity', 'type', 'descriptions', 'mitreattacktatic', 'index', 'query', 'timewindow', 'config', 'recommendation', 'cronexpression', 'status', 'pic', 'comment', 'policytype']