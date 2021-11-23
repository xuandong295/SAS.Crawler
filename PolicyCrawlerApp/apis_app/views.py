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
from .utils import *
# Create your views here.
@csrf_exempt
def export_apis_xls(request):
    return export_data(request)    #export file with option All, Azure, GCP,...

@csrf_exempt
def SearchEngine(request):
    template = 'apis.html'
    return search(request, template)  # search by name, cloud type, ...



@csrf_exempt
def Index(request):
    template = 'apis.html'

    if request.method == "GET":
        apis = Tblapis.objects.all()
        return render(request, template, {'apis': apis})
    if request.method == "POST":
        template = 'apis.html'
        serializer = APISerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
        apis = Tblapis.objects.all()
        return render(request, template, {'apis': apis})
    if request.method == "PUT":
        return update_data(request, template)  # find api by id then update this
    if request.method == "DELETE":
        return delete_data(request, template)


