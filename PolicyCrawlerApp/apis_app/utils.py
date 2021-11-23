from .models import Tblapis
from .serializer import APISerializer
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
    response['Content-Disposition'] = 'attachment; filename="APIs.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Tblapis', cell_overwrite_ok=True)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['No', 'Name', 'Service']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    if request.POST['export-by'] == 'All':
        rows = Tblapis.objects.all().values_list('name', 'service')
    if request.POST['export-by'] == 'Enabled':
        rows = Tblapis.objects.all().filter(status__icontains=1).values_list('name', 'service')
    if request.POST['export-by'] == 'GCP':
        rows = Tblapis.objects.all().filter(status__icontains=1, cloudtype__icontains="gcp").values_list('name',
                                                                                                         'service')
    if request.POST['export-by'] == 'Azure':
        rows = Tblapis.objects.all().filter(status__icontains=1, cloudtype__icontains="azure").values_list('name',
                                                                                                           'service')
    if request.POST['export-by'] == 'AWS':
        rows = Tblapis.objects.all().filter(status__icontains=1, cloudtype__icontains="aws").values_list('name',
                                                                                                         'service')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, 0, row_num, font_style)
            ws.write(row_num, col_num + 1, row[col_num], font_style)

    wb.save(response)
    return response

def search(request, template):
    if request.GET['searchby'] == 'Name':
        apis = Tblapis.objects.all().filter(name__icontains=request.GET.get('text'))
        return render(request, template, {'apis': apis})
    if request.GET['searchby'] == 'Cloud Type':
        apis = Tblapis.objects.all().filter(cloudtype__icontains=request.GET.get('text'))
        return render(request, template, {'apis': apis})
    if request.GET['searchby'] == 'Conformity Status':
        apis = Tblapis.objects.all().filter(conformitystatus__icontains=request.GET.get('text'))
        return render(request, template, {'apis': apis})
    if request.GET['searchby'] == 'Status':
        apis = Tblapis.objects.all().filter(status__icontains=request.GET.get('text'))
        return render(request, template, {'apis': apis})
    if request.GET['searchby'] == 'PIC':
        apis = Tblapis.objects.all().filter(pic__icontains=request.GET.get('text'))
        return render(request, template, {'apis': apis})
    if request.GET['searchby'] == 'Comment':
        apis = Tblapis.objects.all().filter(comment__icontains=request.GET.get('text'))
        return render(request, template, {'apis': apis})

def update_data(request, template):

    put = QueryDict(request.body)
    api = Tblapis.objects.get(pk=put.get("id"))
    print(put.get("comment"))
    serializer = APISerializer(api, data=put)
    if put.get("submit") == 'Update':
        if serializer.is_valid():

            print(put.get("comment"))
            serializer.save()
        print(serializer.errors)
    apis = Tblapis.objects.all()
    return render(request, template, {'apis': apis})

def delete_data(request, template):
    delete = QueryDict(request.body)
    api = Tblapis.objects.get(pk=delete.get("id"))
    print(api)
    api.delete()
    apis = Tblapis.objects.all()
    return render(request, template, {'apis': apis})