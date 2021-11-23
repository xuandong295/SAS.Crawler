from .models import Tblpolicies
from .serializer import ThreatDetectionRuleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import xlwt
from django.http import QueryDict
from django.contrib.auth.models import User

def export_data(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="threat_detection_rules.xls"'
    print(request.POST['export-by'])
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tblpolicies', cell_overwrite_ok=True)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['No', 'Name', 'Cloud Type', 'Severity', 'Type', 'Descriptions', 'Mitre Attack Tactic', 'Index', 'Query'
        , 'Time Window', 'Config', 'Recommendation', 'Cron Expression', 'Status', 'PIC', 'Comment'
               ]
    # print(request.POST['export-by'])
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    if request.POST['export-by'] == 'All':
        rows = Tblpolicies.objects.all().filter(policytype__icontains='detection').values_list('name', 'cloudtype', 'severity', 'type', 'descriptions',
                                                                 'mitreattacktatic',
                                                                 'index', 'query', 'timewindow', 'config',
                                                                 'recommendation', 'cronexpression', 'status', 'pic',
                                                                 'comment')
    if request.POST['export-by'] == 'Enabled':
        rows = Tblpolicies.objects.all().filter(status__icontains=1, policytype__icontains='detection').values_list('name', 'cloudtype',
                                                                                             'severity', 'type',
                                                                                             'descriptions',
                                                                                             'mitreattacktatic',
                                                                                             'index', 'query',
                                                                                             'timewindow', 'config',
                                                                                             'recommendation',
                                                                                             'cronexpression', 'status',
                                                                                             'pic', 'comment')
    if request.POST['export-by'] == 'AWS':
        rows = Tblpolicies.objects.all().filter(status__icontains=1,
                                                            cloudtype__icontains="aws", policytype__icontains='detection').values_list('name', 'cloudtype',
                                                                                                    'severity', 'type',
                                                                                                    'descriptions',
                                                                                                    'mitreattacktatic',
                                                                                                    'index', 'query',
                                                                                                    'timewindow',
                                                                                                    'config',
                                                                                                    'recommendation',
                                                                                                    'cronexpression',
                                                                                                    'status', 'pic',
                                                                                                    'comment')
    if request.POST['export-by'] == 'Azure':
        rows = Tblpolicies.objects.all().filter(status__icontains=1,
                                                            cloudtype__icontains="azure", policytype__icontains='detection').values_list('name',
                                                                                                      'cloudtype',
                                                                                                      'severity',
                                                                                                      'type',
                                                                                                      'descriptions',
                                                                                                      'mitreattacktatic',
                                                                                                      'index', 'query',
                                                                                                      'timewindow',
                                                                                                      'config',
                                                                                                      'recommendation',
                                                                                                      'cronexpression',
                                                                                                      'status', 'pic',
                                                                                                      'comment')
    if request.POST['export-by'] == 'GCP':
        rows = Tblpolicies.objects.all().filter(status__icontains=1,
                                                            cloudtype__icontains="gcp", policytype__icontains='detection').values_list('name', 'cloudtype',
                                                                                                    'severity', 'type',
                                                                                                    'descriptions',
                                                                                                    'mitreattacktatic',
                                                                                                    'index', 'query',
                                                                                                    'timewindow',
                                                                                                    'config',
                                                                                                    'recommendation',
                                                                                                    'cronexpression',
                                                                                                    'status', 'pic',
                                                                                                    'comment')

    rows2 = [" ", " ", "default", " ", "config"]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, 0, row_num, font_style)
            ws.write(row_num, col_num + 1, row[col_num], font_style)

    wb.save(response)
    return response

def search(request, template):
    if request.GET['searchby'] == 'Name':
        rules = Tblpolicies.objects.all().filter(name__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Cloud Type':
        rules = Tblpolicies.objects.all().filter(cloudtype__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Severity':
        rules = Tblpolicies.objects.all().filter(severity__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Type':
        rules = Tblpolicies.objects.all().filter(type__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Descriptions':
        rules = Tblpolicies.objects.all().filter(descriptions__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Mitre Attack tactic':
        rules = Tblpolicies.objects.all().filter(mitreattacktactic__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Index':
        rules = Tblpolicies.objects.all().filter(index__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Query':
        rules = Tblpolicies.objects.all().filter(query__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Time Window':
        rules = Tblpolicies.objects.all().filter(timewindow__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Config':
        rules = Tblpolicies.objects.all().filter(config__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Recommendation':
        rules = Tblpolicies.objects.all().filter(recommendation__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'CronExpression':
        rules = Tblpolicies.objects.all().filter(cronexpression__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Status':
        rules = Tblpolicies.objects.all().filter(status__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'PIC':
        rules = Tblpolicies.objects.all().filter(pic__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})
    if request.GET['searchby'] == 'Comment':
        rules = Tblpolicies.objects.all().filter(comment__icontains=request.GET.get('text'), policytype__icontains='detection')
        return render(request, template, {'rules': rules})


def update_data(request, template):
    put = QueryDict(request.body)
    print(put.get("name"))

    rule = Tblpolicies.objects.get(pk=put.get("id"))

    serializer = ThreatDetectionRuleSerializer(rule, data=put)
    if put.get("submit") == 'Update':
        if serializer.is_valid():
            serializer.save()
        print(serializer.errors)
    rules = Tblpolicies.objects.all()
    return render(request, template, {'rules': rules})

def delete_data(request, template):
    delete = QueryDict(request.body)
    rule = Tblpolicies.objects.get(pk=delete.get("id"))
    print(rule)
    rule.delete()
    rules = Tblpolicies.objects.all()
    return render(request, template, {'rules': rules})