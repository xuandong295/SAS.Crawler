from rest_framework import serializers
from .models import Tblpolicies


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tblpolicies
        fields = ['id', 'name', 'cloudtype', 'service', 'severity', 'descriptions', 'standards', 'query', 'recommendation', 'conformitystatus', 'reviewstatus', 'status', 'pic', 'comment', 'label', 'reference', 'policytype']