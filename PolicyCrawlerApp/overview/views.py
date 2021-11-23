from .models import Tblpolicies, Tblthreatdetectionrules
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.views import View


# Create your views here.

class Index(View):
    template = 'overview.html'

    def get(self, request):
        numberOfEnablePoliciesAws = Tblpolicies.objects.all().filter(cloudtype__icontains='aws', status__icontains=1)
        numberOfEnablePoliciesAzure = Tblpolicies.objects.all().filter(cloudtype__icontains='azure', status__icontains=1)
        numberOfEnablePoliciesGcp = Tblpolicies.objects.all().filter(cloudtype__icontains='gcp', status__icontains=1)
        numberOfCloudConformityPoliciesAws = Tblpolicies.objects.all().filter(cloudtype__icontains='aws')
        numberOfCloudConformityPoliciesAzure = Tblpolicies.objects.all().filter(cloudtype__icontains='azure')
        numberOfCloudConformityPoliciesGcp = Tblpolicies.objects.all().filter(cloudtype__icontains='gcp')
        numberOFReviewPoliciesAws = Tblpolicies.objects.all().filter(cloudtype__icontains='aws', reviewstatus__icontains=1)
        numberOFReviewPoliciesAzure = Tblpolicies.objects.all().filter(cloudtype__icontains='azure', reviewstatus__icontains=1)
        numberOFReviewPoliciesGcp = Tblpolicies.objects.all().filter(cloudtype__icontains='gcp', reviewstatus__icontains=1)
        NewPoliciesAws = Tblpolicies.objects.all().filter(cloudtype__icontains='aws', conformitystatus__icontains="new")
        NewPoliciesAzure = Tblpolicies.objects.all().filter(cloudtype__icontains='azure', conformitystatus__icontains="new")
        NewPoliciesGcp = Tblpolicies.objects.all().filter(cloudtype__icontains='gcp', conformitystatus__icontains="new")
        numberOfEnableRulesAws = Tblthreatdetectionrules.objects.all().filter(cloudtype__icontains='aws', status__icontains=1)
        numberOfEnableRulesAzure = Tblthreatdetectionrules.objects.all().filter(cloudtype='azure', status__icontains=1)
        numberOfEnableRulesGcp = Tblthreatdetectionrules.objects.all().filter(cloudtype='gcp', status__icontains=1)
        totalOfPoliciesGcp = Tblthreatdetectionrules.objects.all().filter(cloudtype__icontains='gcp')
        totalOfPoliciesAws = Tblthreatdetectionrules.objects.all().filter(cloudtype__icontains='aws')
        totalOfPoliciesAzure = Tblthreatdetectionrules.objects.all().filter(cloudtype__icontains='azure')
        return render(request, self.template, {
                                                'numberOfEnablePoliciesAws': numberOfEnablePoliciesAws,
                                                'numberOfEnablePoliciesAzure': numberOfEnablePoliciesAzure,
                                                'numberOfEnablePoliciesGcp': numberOfEnablePoliciesGcp,
                                                'numberOfCloudConformityPoliciesAws': numberOfCloudConformityPoliciesAws,
                                                'numberOfCloudConformityPoliciesAzure': numberOfCloudConformityPoliciesAzure,
                                                'numberOfCloudConformityPoliciesGcp': numberOfCloudConformityPoliciesGcp,
                                                'numberOFReviewPoliciesAws': numberOFReviewPoliciesAws,
                                                'numberOFReviewPoliciesAzure': numberOFReviewPoliciesAzure,
                                                'numberOFReviewPoliciesGcp': numberOFReviewPoliciesGcp,
                                                'NewPoliciesAws': NewPoliciesAws,
                                                'NewPoliciesAzure': NewPoliciesAzure,
                                                'NewPoliciesGcp': NewPoliciesGcp,
                                                'totalOfPoliciesGcp': totalOfPoliciesGcp,
                                                'totalOfPoliciesAzure': totalOfPoliciesAzure,
                                                'totalOfPoliciesAws': totalOfPoliciesAws,
                                                'numberOfEnableRulesAws': numberOfEnableRulesAws,
                                                'numberOfEnableRulesAzure': numberOfEnableRulesAzure,
                                                'numberOfEnableRulesGcp': numberOfEnableRulesGcp
                                                       }
                      )