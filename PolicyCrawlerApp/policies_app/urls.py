from django.urls import path, include
from .views import Index, SearchEngine, export_policies_xls
urlpatterns = [
    path('policy/', Index, name='policy'),
    path('search-policy/', SearchEngine, name='search-data-policy'),
    path(r'^export-policies/xls/$', export_policies_xls, name='export_policies_xls')
]
