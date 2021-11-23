from .models import Tblpolicies
from .serializer import PolicySerializer
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
    response['Content-Disposition'] = 'attachment; filename="policies.xls"'
    print(request.POST['export-by'])
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tblpolicies', cell_overwrite_ok=True)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['No', 'Name', 'Cloud Type', 'Severity', 'Status', 'Query', 'Standards', 'Descriptions', 'Recommendation'
        , 'Label', 'Save Search ID', 'Save Search Name', 'Mode', 'Last Modify Time', 'Policy Type']
    # print(request.POST['export-by'])
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    if request.POST['export-by'] == 'All':
        rows = Tblpolicies.objects.all().filter(policytype__icontains='config').values_list('name', 'cloudtype', 'severity', 'status', 'query', 'standards',
                                                     'descriptions', 'recommendation', 'label')
    if request.POST['export-by'] == 'Enabled':
        rows = Tblpolicies.objects.all().filter(status__icontains=1, policytype__icontains='config').values_list('name', 'cloudtype', 'severity',
                                                                                 'status', 'query', 'standards',
                                                                                 'descriptions', 'recommendation',
                                                                                 'label')
    if request.POST['export-by'] == 'AWS':
        rows = Tblpolicies.objects.all().filter(status__icontains=1, cloudtype__icontains="aws", policytype__icontains='config').values_list('name',
                                                                                                             'cloudtype',
                                                                                                             'severity',
                                                                                                             'status',
                                                                                                             'query',
                                                                                                             'standards',
                                                                                                             'descriptions',
                                                                                                             'recommendation',
                                                                                                             'label')
    if request.POST['export-by'] == 'Azure':
        rows = Tblpolicies.objects.all().filter(status__icontains=1, cloudtype__icontains="azure", policytype__icontains='config').values_list('name',
                                                                                                               'cloudtype',
                                                                                                               'severity',
                                                                                                               'status',
                                                                                                               'query',
                                                                                                               'standards',
                                                                                                               'descriptions',
                                                                                                               'recommendation',
                                                                                                               'label')
    if request.POST['export-by'] == 'GCP':
        rows = Tblpolicies.objects.all().filter(status__icontains=1, cloudtype__icontains="gcp", policytype__icontains='config').values_list('name',
                                                                                                             'cloudtype',
                                                                                                             'severity',
                                                                                                             'status',
                                                                                                             'query',
                                                                                                             'standards',
                                                                                                             'descriptions',
                                                                                                             'recommendation',
                                                                                                             'label')

    rows2 = [" ", " ", "default", " ", "config"]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, 0, row_num, font_style)
            ws.write(row_num, col_num + 1, row[col_num], font_style)
            for i in range(0, len(rows2)):
                ws.write(row_num, len(row) + i + 1, rows2[i], font_style)
    wb.save(response)
    return response

def search(request, template):

    if request.GET['searchby'] == 'Name':
        policies = Tblpolicies.objects.all().filter(name__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.GET['searchby'] == 'Cloud Type':
        policies = Tblpolicies.objects.all().filter(cloudtype__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.GET['searchby'] == 'Service':
        policies = Tblpolicies.objects.all().filter(service__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.GET['searchby'] == 'Severity':
        policies = Tblpolicies.objects.all().filter(severity__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.GET['searchby'] == 'Standards':
        policies = Tblpolicies.objects.all().filter(standards__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.GET['searchby'] == 'Review Status':
        policies = Tblpolicies.objects.all().filter(reviewstatus__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.GET['searchby'] == 'Status':
        policies = Tblpolicies.objects.all().filter(status__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.GET['searchby'] == 'PIC':
        policies = Tblpolicies.objects.all().filter(pic__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})
    if request.GET['searchby'] == 'Query':
        policies = Tblpolicies.objects.all().filter(query__icontains=request.GET.get('text'), policytype__icontains='config')
        return render(request, template, {'policies': policies})

def update_data(request, template):
    put = QueryDict(request.body)
    print(put.get("id"))
    print(put.get("name"))
    # print(put.get("cloudtype"))
    print(put.get("severity"))
    # print(put.get("descriptions"))
    # print(put.get("standards"))
    # print(put.get("query"))
    # print(put.get("recommendation"))
    # print(put.get("conformitystatus"))
    # print(put.get("reviewstatus"))
    # print(put.get("status"))


    #id', 'name', 'cloudtype', 'severity', 'descriptions', 'standards', 'query', 'recommendation', 'conformitystatus', 'reviewstatus', 'status', 'pic', 'comment', 'label', 'reference', 'p
    policy = Tblpolicies.objects.get(id=put.get("id"))

    serializer = PolicySerializer(policy, data=put)
    if put.get("submit") == 'Update':
        if serializer.is_valid():
            serializer.save()
        print(serializer.errors)
    rules = Tblpolicies.objects.all()
    return render(request, template, {'rules': rules})

def delete_data(request, template):
    delete = QueryDict(request.body)
    policy = Tblpolicies.objects.get(pk=delete.get("id"))
    print(policy)
    policy.delete()
    policies = Tblpolicies.objects.all()
    return render(request, template, {'policies': policies})