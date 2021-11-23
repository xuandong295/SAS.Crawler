from django.urls import path, include
from .views import Index, SearchEngine, export_apis_xls
urlpatterns = [
    path('api/', Index, name='api'),
    # path('policy/search/', SearchEngine.as_view(), name='search'),
    path('search-api/', SearchEngine, name='search-data-api'),
    path(r'^export-apis/xls/$', export_apis_xls, name='export_apis_xls')
]
